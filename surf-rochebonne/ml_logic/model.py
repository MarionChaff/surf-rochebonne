
from tensorflow.keras import Sequential, layers, optimizers, callbacks, Input
import numpy as np

class Model:

    def __init__(self):
        self.model = None

    def fit(self, X, y):

        # Optimizer
        optimizer = optimizers.Adam(
            learning_rate=optimizers.schedules.PolynomialDecay(
            initial_learning_rate=0.001,
            decay_steps=10000,
            end_learning_rate=0.0001,
            power=2.0))

        # Neural network model architecture
        self.model = Sequential()
        self.model.add(layers.Input(shape=(X.shape[-1],)))
        self.model.add(layers.Dense(20, activation='relu'))
        self.model.add(layers.Dense(15, activation='relu'))
        self.model.add(layers.Dense(20, activation='relu'))
        self.model.add(layers.Dense(20, activation='relu'))
        self.model.add(layers.Dense(15, activation='relu'))
        self.model.add(layers.Dense(20, activation='relu'))
        self.model.add(layers.Dense(4, activation='softmax'))

        # Compiler
        self.model.compile(optimizer=optimizer,loss='categorical_crossentropy',metrics=['accuracy'])

        try :
            # Fit
            self.model.fit(X, y, batch_size=32, epochs=100)
            print("✅ Model fitted")
        except Exception as e:
            print("❌ Exception during fitting")

        return None

    def predict(self, X):
        return np.argmax(self.model.predict(X), axis=1)
