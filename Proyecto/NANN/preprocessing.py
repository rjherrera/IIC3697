import numpy as np
import json
from collections import Counter

# Parámetros
GLOVE_SIZE = 50
CONTEXT_SIZE = 600
QUESTION_SIZE = 40


def get_embeddings(filename):
    with open(filename, 'rt', encoding="utf8") as fp:
        embeddings = {}
        for line in fp:
            values = line.split()
            word = values[0]
            coefs = np.asarray(values[1:], dtype='float32')
            embeddings[word] = coefs
        fp.close()
        return embeddings


def string_to_matrix(string, rows, cols, embeddings):
    matrix = np.empty([rows, cols], dtype='float32')
    i = 0
    for word in string:
        if word in embeddings:
            matrix[i] = embeddings[word]
            i += 1
    for j in range(i, rows):
        matrix[j] = np.zeros(cols)
    return matrix


def generate_data(filename, batch_memory):
    # Definimos el diccionario de embeddings
    embeddings = get_embeddings('glove.6B.{}d.txt'.format(GLOVE_SIZE))

    # Memory
    memory_usage = int(batch_memory * (10 ** 9))
    batch_size = memory_usage // ((CONTEXT_SIZE * GLOVE_SIZE + QUESTION_SIZE * GLOVE_SIZE + 2) * 8)

    # Cargamos el dataset y dejamos los símbolos separados de las palabras
    with open(filename) as fp:
        data = fp.read().lower()
        for symbol in ['(', ';', '=', '|', '\\', '_', '!', '+', '`', '@', '"',
                       '%', '.', '?', ')', "'", '$', '^', '<', ':', '#', '-',
                       '&', '*', '~', '>', '/', ',']:
            data.replace(symbol, " " + symbol + " ")
        data = json.loads(data)
        data = data["data"]

    context_set = np.empty([batch_size, CONTEXT_SIZE, GLOVE_SIZE])
    question_set = np.empty([batch_size, QUESTION_SIZE, GLOVE_SIZE])
    answer_set = np.empty([batch_size, 2])
    i = 0
    for sample in data:
        title = sample["title"]
        for paragraph in sample["paragraphs"]:
            context = paragraph["context"].strip().split()[:CONTEXT_SIZE]
            context_glove = string_to_matrix(context, CONTEXT_SIZE, GLOVE_SIZE, embeddings)
            for qa in paragraph["qas"]:
                id_ = qa["id"]
                question = qa["question"].strip().split()[:QUESTION_SIZE]
                answers = [(a["answer_start"], a["answer_start"] + len(a["text"])) for a in qa["answers"]]
                start, end = Counter(answers).most_common(1)[0][0]
                if end > CONTEXT_SIZE - 1:
                    continue
                answer = np.array([start, end], dtype=np.uint8)
                question_glove = string_to_matrix(question, QUESTION_SIZE, GLOVE_SIZE, embeddings)
                context_set[i] = context_glove
                question_set[i] = question_glove
                answer_set[i] = answer
                i += 1

                if i == batch_size:
                    yield [context_set, question_set], answer_set

                    i = 0
                    context_set = np.empty([batch_size, CONTEXT_SIZE, GLOVE_SIZE])
                    question_set = np.empty([batch_size, QUESTION_SIZE, GLOVE_SIZE])
                    answer_set = np.empty([batch_size, 2])

    yield [context_set[:i-1], question_set[:i-1]], answer_set[:i-1]
