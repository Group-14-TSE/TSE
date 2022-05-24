import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
#from sklearn.metrics import accuracy_score

f = open("Passwords.txt", "r")
f.readline()
file = []
l = []
strength = []
for lines in f:
    file.append(tuple(map(str, lines.split())))
for lines in file:
    l.append(lines[0])

for lines in file:
    strength.append(lines[1])
#
def values(listy):
    result = []

    for i in listy:
        length = 0
        lowercase = 0
        uppercase = 0
        number = 0
        symbol = 0
        chars = set('!"£$%^&*(),')
        if any((c in chars) for c in i):
            symbol = 1

        chars = set('QWERTYUIOPASDFGHJKLZXCVBNM')
        if any((c in chars) for c in i):
            uppercase = 1

        chars = set('qwertyuiopasdfghjklzxcvbnm')
        if any((c in chars) for c in i):
            lowercase = 1

        chars = set('1234567890')
        if any((c in chars) for c in i):
            number = 1

        if len(i) > 8:
            length = 1

        result.append((length, lowercase, uppercase, number, symbol))
    return result


def strengthValues(listy):
    result = []
    for i in listy:
        if i == "weak":
            result.append((1, 0, 0))
        elif i == "medium":
            result.append((0, 1, 0))
        elif i == "strong":
            result.append((0, 0, 1))
    return result




inputValues = values(l)
print(inputValues)
targets = strengthValues(strength)
print(targets)

x_train, x_test, y_train, y_test = train_test_split(inputValues, targets, test_size=0.2, random_state=0)

print(x_train)
print(y_train)

inputs = keras.Input(shape = (5,))
dense = layers.Dense(8, activation= "relu")
dense_1 = layers.Dense(8, activation= "relu")
dense_2 = layers.Dense(3, activation= "sigmoid")

x = dense(inputs)
x = dense_1(x)
outputs = dense_2(x)

model = keras.Model(inputs=inputs, outputs=outputs, name="test_model")
model.summary()

model.compile(loss='binary_crossentropy', optimizer='sgd', metrics='accuracy')
model.fit(x_train, y_train, epochs=2000, batch_size=5)

y_hat = model.predict(x_test)
#y_hat = [0 if val < 0.5 else 1 for val in y_hat]

#accuracy_score(y_test, y_hat)

model.save('tfmodel')
print("done")
