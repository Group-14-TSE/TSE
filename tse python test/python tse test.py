from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import load_model

## opens traing file.
def openTrainFile():
    f = open("Passwords.txt", "r")
    f.readline()
    file = []
    # adds all data in file to a list of tuples.
    for lines in f:
        file.append(tuple(map(str, lines.split())))
    return file

## isolates passwords.
def trainingInputs():
    file = openTrainFile()
    l = []
    # adds all passwords to list.
    for lines in file:
        l.append(lines[0])
    return l

## isolates target password strengths.
def trainingTargets():
    file = openTrainFile()
    strength = []
    # adds all traget strengths to a list.
    for lines in file:
        strength.append(lines[1])
    return strength

## sets input values ready to be inputted into the neural network.
def values(listy):
    result = []
    # loops for all passwords entered.
    for i in listy:
        length = 0
        lowercase = 0
        uppercase = 0
        number = 0
        symbol = 0
        
        # checks for any symbols in password.
        chars = set('!"£$%^&*(),')
        if any((c in chars) for c in i):
            # sets input value to 1 if symbols are present.
            symbol = 1

        # checks for any uppercase letters in password.
        chars = set('QWERTYUIOPASDFGHJKLZXCVBNM')
        if any((c in chars) for c in i):
            # sets input value to 1 if uppercase letters are present.
            uppercase = 1
            
        # checks for any lowercase letters in password.
        chars = set('qwertyuiopasdfghjklzxcvbnm')
        if any((c in chars) for c in i):
            # sets input value to 1 if lowercase letters are present.
            lowercase = 1

        # checks for any numbers in password.
        chars = set('1234567890')
        if any((c in chars) for c in i):
            # sets input value to 1 if numbers are present
            number = 1

        # checks if the password length is longer than 8.
        if len(i) > 8:
            # sets input value to 1 if the length is longer than 8.
            length = 1

        # checks if a password has been entered
        if i == "N/A":
            # sets all input values to 0 if no password was entered.
            length = lowercase = uppercase = number = symbol = 0

        # adds input values to a list of tuples.
        result.append((length, lowercase, uppercase, number, symbol))
    # returns list of tuples.
    return result

## sets expected output values for each password.
def strengthValues():
    listy = trainingTargets()
    result = []
    for i in listy:
        # loops for all expected outputs.
        # value of 1 represnts expected output node.
        if i == "weak":
            result.append((1, 0, 0))
        elif i == "medium":
            result.append((0, 1, 0))
        elif i == "strong":
            result.append((0, 0, 1))
    return result


## trains the neural network.
def training():
    # sets input values.
    inputValues = values(trainingInputs())
    
    # sets target values.
    targets = strengthValues()

    # splits 80% of data to training at 20% to testing.
    x_train, x_test, y_train, y_test = train_test_split(inputValues, targets, test_size=0.2, random_state=0)


    # creates the layers of the neural network.
    inputs = keras.Input(shape = (5,))
    dense = layers.Dense(8, activation= "relu")
    dense_1 = layers.Dense(8, activation= "relu")
    dense_2 = layers.Dense(3, activation= "sigmoid")
    
    # links the layers of the neural network.
    x = dense(inputs)
    x = dense_1(x)
    outputs = dense_2(x)

    # creates the model of the neural network.
    model = keras.Model(inputs=inputs, outputs=outputs, name="test_model")

    # sets the training parameters of the neural network.
    model.compile(loss='binary_crossentropy', optimizer='sgd', metrics='accuracy')

    #trains the neural network.
    model.fit(x_train, y_train, batch_size=5, epochs=1000)

    # saves the neural network
    model.save('tfmodel')

    del model


def openTestFile():
    # opens up test file.
    f = open("Test_Network_1.txt")
    f.readline()
    file = []
    # adds all data to list of tuples.
    for lines in f:
        file.append(tuple(map(str, lines.split())))
    return file
    
def testInput():
    file = openTestFile()
    passwords = []
    for lines in file:
        if len(lines) > 0:
            passwords.append(lines[5]) #### change from 5 to 1 with new data set
    return passwords

## writes password strengths to file.
def writeToFile(outcome):
    f = open("network security posture.txt", "w")
    file = openTestFile()
    line = 0
    for i in range(len(outcome)):
        if len(file[i]) > 0:
            # writes device name.
            f.write(file[i][0])
            f.write(" ")
            # writes password.
            f.write(file[i][5]) #### change from 5 to 1 with new data set
            f.write(" ")
            # writes password strength.
            f.write(outcome[line])
            f.write("\n")
            line += 1
    print("Network Scurity Posture.txt has been updated with your results")
            


## decides password strength.
def testing():
    # loads neural network.
    model = load_model('tfmodel')

    # sets test input data.
    testData = values(testInput())
    
    # predicts password strength.
    predictions = model.predict(testData)
    outcome = []

    # makes output of neural network understandable.
    for i in range(len(predictions)):
        # chooses highes activation of node from output layer.
        if predictions[i][0] > predictions[i][1] and predictions[i][0] > predictions[i][2]:
            outcome.append("weak")
        elif predictions[i][1] > predictions[i][0] and predictions[i][1] > predictions[i][2]:
            outcome.append("medium")
        elif predictions[i][2] > predictions[i][0] and predictions[i][2] > predictions[i][1]:
            outcome.append("strong")

    # writes to file.
    writeToFile(outcome)
    
def menu():
    done = False
    while done == False:
        print("Please enter whether you would like to 'train' or 'test' the neural network. ")
        print("**NOTE** If the network has already been trained then training is not necessary")
        choice = input("If you are finished please enter 'quit' or 'q'.")
        user_input = choice.lower()
        if user_input == "train":
            training()
        elif user_input == "test":
            testing()
        elif user_input == "quit" or user_input == "q":
            done = True
        else:
            print("input is invalid")


menu()
