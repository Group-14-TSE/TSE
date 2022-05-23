f = open("Test_Network_1.txt", "r")
f.readline()
l = []
for x in f:
    l.append(tuple(map(str, x.split())))



def printName(listy):
    for i in range(0, len(listy)):
        if len(listy[i]) > 0:
            print(listy[i][0])

def printPort(listy):
    for i in range(0, len(listy)):
        if len(listy[i]) > 0:
            print(listy[i][1])

def printIP(listy):
    for i in range(0, len(listy)):
        if len(listy[i]) > 0:
            print(listy[i][2])

def printSubnet(listy):
    for i in range(0, len(listy)):
        if len(listy[i]) > 0:
            print(listy[i][3])

def printDefaultGateway(listy):
    for i in range(0, len(listy)):
        if len(listy[i]) > 0:
            print(listy[i][4])

def printPassword(listy):
    for i in range(0, len(listy)):
        if len(listy[i]) > 0:
            print(listy[i][5])

def printAll(listy):
    for i in listy:
        print(i)

def returnPasswords(listy):
    passwords = []
    for i in range(0, len(listy)):
        if len(listy[i]) >= 6:
            passwords.append(listy[i][5])
    return passwords

def returnPasswordsBool(listy):
    passwordsBool = []
    for i in range(0, len(listy)):
        if len(listy[i]) >= 6:
            if listy[i][5] != "N/A":
                passwordsBool.append(1)
            else:
                passwordsBool.append(0)
    return passwordsBool

def passwordsBoolCheck(passwords, bools):
    for i in range(len(passwords)):
        print(passwords[i], bools[i])

def returnPorts(listy):
    ports = []
    for i in range(0, len(listy)):
        if len(listy[i]) >= 2:
            ports.append(listy[i][2])
    return ports

def returnPortsBool(listy):
    portsBool = []
    for i in range(0, len(listy)):
        if len(listy[i]) != 0:
            if listy[i][2] != "N/A":
                portsBool.append(1)
            else:
                portsBool.append(0)
    return portsBool

def portsBoolCheck(ports, bools):
    for i in range(0, len(ports)):
        print(ports[i], bools[i])

#printName(l)
#printPort(l)
#printIP(l)
#printSubnet(l)
#printDefaultGateway(l)
#printPassword(l)
#printAll(l)
passwords = returnPasswords(l)
passwordsBool = returnPasswordsBool(l)
passwordsBoolCheck(passwords, passwordsBool)
portsBool = returnPortsBool(l)
ports = returnPorts(l)
portsBoolCheck(ports, portsBool)
