import re
import numpy as np
from tabulate import tabulate

tokens = []
nonTerm = []
Regex = []
inputStack = []
parserStack = ['$', 'S']
Data = []
predictKeys = []
predictValues = []
rows = 0


def setParser(lX, cfg):
    global tokens, nonTerm, Regex, inputStack
    tokens = lX.tokens
    nonTerm = cfg.NonTerm
    Regex = cfg.Regex
    for token in tokens:
        inputStack = np.append(inputStack, token)
    inputStack = np.append(inputStack, '$')
    inputStack = np.flip(inputStack)


def ToString(list):
    string = '$ '
    for st in list[:-1]:
        string = string + st + ' '
    return string


def checkRegex(key):
    if key in [key for key in Regex]:
        return True
    return False


def pop(stack):
    return np.delete(stack, -1)


def stackMatch():
    global Data, parserStack, inputStack, predictKeys, predictValues
    Data[-1] = "Predict: {} --> {}".format(parserStack[-1], inputStack[-1])
    predictKeys.append(parserStack[-1])
    predictValues.append(inputStack[-1])
    parserStack = pop(parserStack)
    parserStack = np.append(parserStack, inputStack[-1])
    appendData()
    DataMatch()


def DataMatch():
    global Data, parserStack, inputStack
    Data[-1] = "Match: {}".format(inputStack[-1])
    inputStack = pop(inputStack)
    parserStack = pop(parserStack)
    appendData()


def appendData():
    global Data, parserStack, inputStack, rows
    revInputStack = np.flip(inputStack)
    revParserStack = np.flip(parserStack)
    Data = np.append(Data, [ToString(revParserStack), ToString(revInputStack), ''])
    rows += 1


def predictStr(choice):
    global Data, parserStack, inputStack, predictKeys, predictValues
    string = choice.split(' ')
    string.reverse()
    Data[-1] = ('Predict: {} --> {}'.format(parserStack[-1], choice))
    predictKeys.append(parserStack[-1])
    predictValues.append(choice)
    parserStack = pop(parserStack)
    for letter in string:
        parserStack = np.append(parserStack, letter)
    appendData()


def LLparser():
    global Data, parserStack, inputStack, rows, predictKeys, predictValues
    appendData()
    while True:
        if inputStack[-1] == '$' and parserStack[-1] == '$':
            Data[-1] = 'Accept!!'
            return True
        if parserStack[-1] == '$' and inputStack[-1] != '$':
            Data[-1] = 'Reject!!'
            return False
        if parserStack[-1] == inputStack[-1]:
            DataMatch()
        elif checkRegex(parserStack[-1]):
            if re.fullmatch(Regex[parserStack[-1]], inputStack[-1]):
                stackMatch()
            else:
                Data[-1] = 'Reject!!'
                return False
        elif parserStack[-1] in [key for key in nonTerm]:
            if isinstance(nonTerm[parserStack[-1]], str):
                predictStr(nonTerm[parserStack[-1]])
            else:
                choice = decider(parserStack[-1], inputStack[-1])
                if choice == -1:
                    Data[-1] = 'Predict: {} --> λ'.format(parserStack[-1])
                    predictKeys.append(parserStack[-1])
                    predictValues.append('λ')
                    parserStack = pop(parserStack)
                    appendData()
                elif choice == -2:
                    Data[-1] = 'Reject!!'
                    return False
                else:
                    predictStr(nonTerm[parserStack[-1]][choice])
        else:
            Data[-1] = 'Reject!!'
            return False


def decider(key, currentToken):
    index = 0
    for choice in nonTerm[key]:
        choice = choice.split(' ')
        if deciderParser(choice[0], currentToken):
            return index
        index += 1
    if nonTerm[key][-1] == '':
        return -1
    return -2


def deciderParser(key, currentToken):
    if key == currentToken:
        return True
    elif checkRegex(key):
        return re.fullmatch(Regex[key], currentToken)
    elif key in [keys for keys in nonTerm]:
        if isinstance(nonTerm[key], str):
            string = nonTerm[key].split(' ')
            return deciderParser(string[0], currentToken)
        else:
            choice = decider(key, currentToken)
            if choice == -1:
                return True
            elif choice == -2:
                return False
            else:
                return True


def mapping():
    global Data, rows
    Data.shape = (rows, 3)
    table = tabulate(Data, headers=['Parser Stack', 'Input Stack', 'Action'])
    return table
