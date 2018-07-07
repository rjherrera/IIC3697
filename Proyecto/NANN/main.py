from keras import Sequential
from keras.layers import Dense, LSTM, Merge, Bidirectional
from keras.callbacks import ModelCheckpoint
from keras.callbacks import Callback

import json
import numpy as np

from preprocessing import generate_data, GLOVE_SIZE, CONTEXT_SIZE, QUESTION_SIZE
from testing import generate_predictions


class MdelafMetric(Callback):

    def __init__(self, model, validation_data):
        super().__init__()
        self.set_model(model)
        self.history = []
        self.validation_dataset = validation_data

    def on_epoch_end(self, epoch, logs=None):
        value = self.mdelaf_metric()
        self.history.append(value)
        print("Mdelaf metric: {}".format(value))

    def mdelaf_metric(self):
        X_true, y_true = self.validation_dataset
        y_target = self.model.predict(X_true)
        total_score = 0
        for i in range(len(X_true)):
            start, end = np.array(y_target[i], dtype=np.int8)
            start_true, end_true = np.array(y_true[i], dtype=np.int8)
            true_indexes = set(range(start_true, end_true + 1))
            target_indexes = set(range(start, end + 1))
            total_score += len(true_indexes.intersection(target_indexes)) / len(true_indexes)
        return total_score / len(X_true)


context_output_dim = GLOVE_SIZE
context_input_dim = GLOVE_SIZE
context_sequence_length = CONTEXT_SIZE

question_output_dim = GLOVE_SIZE
question_input_dim = GLOVE_SIZE
question_sequence_length = QUESTION_SIZE

# Definimos el modelo
context_branch = Sequential()
context_branch.add(Bidirectional(LSTM(context_output_dim, name="context_layer"),
                                 input_shape=(context_sequence_length, context_input_dim)))

question_branch = Sequential()
question_branch.add(Bidirectional(LSTM(question_output_dim, name="question_layer"),
                                  input_shape=(question_sequence_length, question_input_dim)))

model = Sequential()
model.add(Merge([context_branch, question_branch], mode='concat'))
model.add(Dense(200, activation="relu"))
model.add(Dense(2, activation="relu"))

model.compile(optimizer='adam', loss='mse')
model.summary()


TRAIN_OR_TEST = "train"
WEIGHTS = "model_weights.h5"
PREDICTION_OUTPUT = "squad/custom-mse-pred.txt"

if TRAIN_OR_TEST == "train":
    # Definimos los set de datos
    validation_dataset = next(generate_data("squad/dev-v1.1.json", batch_memory=1))
    X, y = next(generate_data("squad/train-v1.1.json", batch_memory=8))

    # Definimos las métricas
    mdelaf_metric = MdelafMetric(model, validation_dataset)
    checkpoint = ModelCheckpoint(filepath=WEIGHTS, save_weights_only=True)

    # Entrenamos
    history = model.fit(X, y, epochs=15, batch_size=128, validation_split=0.2,
                        shuffle=True, callbacks=[checkpoint, mdelaf_metric])

    with open("history.json", "wt") as fp:
        json.dump([history.history, mdelaf_metric.history], fp)

else:
    #model.load_weights(WEIGHTS)
    generate_predictions(model, "squad/dev-v1.1.json", PREDICTION_OUTPUT)
