import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import load_model
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
            
        if i == "N/A":
            length = lowercase = uppercase = number = symbol = 0

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



def training(l, strenght):
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
    model.fit(x_train, y_train, batch_size=5, epochs=1000)

    y_hat = model.predict(x_test)
    #y_hat = [0 if val < 0.5 else 1 for val in y_hat]

    #accuracy_score(y_test, y_hat)

    model.save('tfmodel')

    del model

    model = load_model('tfmodel')
    print("done")

#training(l, strength)

def openTestFile():
    f = open("Test_Network_1.txt")
    f.readline()
    file = []
    for lines in f:
        file.append(tuple(map(str, lines.split())))
    print(file)
    return file
    
def testInput():
    file = openTestFile()
    passwords = []
    for lines in file:
        if len(lines) > 0:
            passwords.append(lines[5])
    for i in range(len(passwords)):
        print(passwords[i], len(passwords[i]))
    return passwords


def writeToFile(outcome):
    f = open("network security posture.txt", "w")
    #f.write("ok this is cool")
    file = openTestFile()
    line = 0
    for i in range(len(outcome)):
        if len(file[i]) > 0:
            f.write(file[i][0])
            f.write(" ")
            f.write(file[i][5])
            f.write(" ")
            f.write(outcome[line])
            f.write("\n")
            line += 1



def testing(l):
    model = load_model('tfmodel')
    print("loaded")

    testData = values(testInput())
    
    
    predictions = model.predict(testData)
    outcome = []

    for i in range(len(predictions)):
        if predictions[i][0] > predictions[i][1] and predictions[i][0] > predictions[i][2]:
            outcome.append("weak")
        elif predictions[i][1] > predictions[i][0] and predictions[i][1] > predictions[i][2]:
            outcome.append("medium")
        elif predictions[i][2] > predictions[i][0] and predictions[i][2] > predictions[i][1]:
            outcome.append("strong")
        else:
            print("something is wrong")
    print(outcome)
    writeToFile(outcome)
    



    
testing(l)
