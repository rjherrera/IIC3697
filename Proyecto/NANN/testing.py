from preprocessing import get_embeddings, string_to_matrix, GLOVE_SIZE, CONTEXT_SIZE, QUESTION_SIZE

import json
import numpy as np


def generate_predictions(model, filepath, destination):
    # Definimos el diccionario de embeddings
    embeddings = get_embeddings('glove.6B.{}d.txt'.format(GLOVE_SIZE))

    # Cargamos el dataset y dejamos los símbolos separados de las palabras
    with open(filepath) as fp:
        data = fp.read().lower()
        for symbol in ['(', ';', '=', '|', '\\', '_', '!', '+', '`', '@', '"',
                       '%', '.', '?', ')', "'", '$', '^', '<', ':', '#', '-',
                       '&', '*', '~', '>', '/', ',']:
            data.replace(symbol, " " + symbol + " ")
        data = json.loads(data)
        data = data["data"]

    predictions = {}
    for sample in data:
        title = sample["title"].strip().replace(" ", "_").lower()[:40]
        for paragraph in sample["paragraphs"]:
            context = paragraph["context"].strip().split()[:CONTEXT_SIZE]
            context_glove = string_to_matrix(context, CONTEXT_SIZE, GLOVE_SIZE, embeddings)
            context_glove = np.expand_dims(context_glove, axis=0)
            for qa in paragraph["qas"]:
                id_ = qa["id"]
                question = qa["question"].strip().split()[:QUESTION_SIZE]
                question_glove = string_to_matrix(question, QUESTION_SIZE, GLOVE_SIZE, embeddings)
                question_glove = np.expand_dims(question_glove, axis=0)
                y_predicted = model.predict([context_glove, question_glove])[0]
                start, end = np.array(y_predicted, dtype=np.uint8)

                if (end <= start) or (end >= len(context)):
                    print("Skipped ", start, end)
                    continue

                answer = " ".join(context[start:end + 1])
                predictions[id_] = answer
                print(question, " > ", answer)

    with open(destination, "wt") as fp:
        json.dump(predictions, fp)




