import re
import numpy as np
from tabulate import tabulate  # table the data

reject = False
tokens = []
nonTerm =[]
term = []
inputStack = []
parserStack = ['$', 'S']
Data = []
i = 0

def setParser(lX, cfg):
    global tokens, nonTerm, term, inputStack
    tokens = lX.tokens
    nonTerm = cfg.NonTerm
    term = cfg.Term
    for token in tokens:
        inputStack = np.append(inputStack, token.string)
    inputStack = np.append(inputStack, '$')
    inputStack = np.flip(inputStack)



def checkTerm(key):
    if key in [key for key in term]:
        return True
    return False

def pop(stack):
    return np.delete(stack, -1)

def stackMatch():
    global Data, parserStack, inputStack, i
    key = parserStack[-1]
    parserStack = pop(parserStack)
    parserStack = np.append(parserStack, inputStack[-1])
    Data[-1] = "Predict: {} --> {}".format(key, inputStack[-1])
    appendData()
    i += 1
    Data[-1] = "Match: {}".format(inputStack[-1])
    inputStack = pop(inputStack)
    parserStack = pop(parserStack)
    appendData()
    i += 1

def ToString(list):
    string = '$ '
    for st in list[:-1]:
        string = string + st + ' '
    return string

def appendData():
    global Data, i, parserStack, inputStack
    revInputStack = np.flip(inputStack)
    revParserStack = np.flip(parserStack)
    Data = np.append(Data, [ToString(revParserStack), ToString(revInputStack), ''])

def LLparser():
    global reject, Data, parserStack, inputStack, i
    appendData()
    i += 1
    while not reject:
        if inputStack[-1] == '$' and parserStack[-1] == '$':
            Data[-1] = 'Accept!!'
            break
        if parserStack[-1] == '$' and inputStack[-1] != '$':
            Data[-1] = 'Reject!!'
            break
        if parserStack[-1] == inputStack[-1]:
            Data[-1] = "Match: {}".format(inputStack[-1])
            inputStack = pop(inputStack)
            parserStack = pop(parserStack)
            appendData()
            i += 1
        elif checkTerm(parserStack[-1]):
            if re.match(term[parserStack[-1]], inputStack[-1]):
                stackMatch()
            else:
                Data[-1] = 'Reject!!'
                reject = True
                break
        elif isinstance(nonTerm[parserStack[-1]], str):
            string = nonTerm[parserStack[-1]].split(' ')
            string.reverse()
            Data[-1] = ('Predict: {} --> {}'.format(parserStack[-1], nonTerm[parserStack[-1]]))
            parserStack = pop(parserStack)
            for letter in string:
                parserStack = np.append(parserStack, letter)
            appendData()
            i += 1
        else:
            choice = decider(parserStack[-1], inputStack[-1])
            if choice == -1:
                Data[-1] = 'Predict: {} --> λ'.format(parserStack[-1])
                parserStack = pop(parserStack)
                appendData()
                i += 1
            elif choice == -2:
                Data[-1:-1] = 'Reject!!'
                reject = True
                break
            else:
                string = nonTerm[parserStack[-1]][choice].split(' ')
                string.reverse()
                Data[-1] = 'Predict: {} --> {}'.format(parserStack[-1], nonTerm[parserStack[-1]][choice])
                parserStack = pop(parserStack)
                for letter in string:
                    parserStack = np.append(parserStack, letter)
                appendData()
                i += 1


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
    elif checkTerm(key):
        return re.match(term[key], currentToken)
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
    global Data, i
    Data.shape = (i, 3)
    table = tabulate(Data, headers=['parser Stack', 'input Stack', 'Action'])
    return table
