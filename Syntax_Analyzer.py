import re
import numpy as np
from tabulate import tabulate  # table the data

reject = False
tokens = []
nonTerm =[]
term = []
inputStack =[]
parserStack = ['S']
Data = np.empty((1, 1))
i= 0

def setParser(lX, cfg):
    global tokens, nonTerm, term, inputStack
    tokens = lX.tokens
    nonTerm = cfg.NonTerm
    term = cfg.Term
    for token in tokens:
        inputStack.append(token.string)
    print(inputStack)
    inputStack.reverse()
    #print(inputStack)


    # def match(self, key, s):
    #     return re.match(self.Term[key], s)

def checkTerm(key):
    if key in [key for key in term]:
        return True
    return False

def stackMatch():
    global Data, parserStack, inputStack, i
    key = parserStack[-1]
    parserStack.pop()
    parserStack.append(inputStack[-1])
    Data[-1][-1] = "Predict: {} --> {}".format(key, inputStack[-1])
    Data = np.append(Data, [parserStack, inputStack, 'a'])
    i += 1
    inputStack.pop()
    parserStack.pop()
    Data = np.append(Data, [parserStack, inputStack, 'a'])
    i += 1

def LLparser():
    global reject, Data, parserStack, inputStack, i
    Data = np.append(Data, [parserStack, inputStack, 'a'])
    i += 1
    while not reject:
        if inputStack == [] and parserStack == []:
            break;
        if parserStack[-1] == inputStack[-1]:
            Data[-1][-1] = "Match {}".format(inputStack[-1])
            inputStack.pop()
            parserStack.pop()
            Data = np.append(Data, [parserStack, inputStack, 'a'])
            i += 1
        elif checkTerm(parserStack[-1]):
            if re.match(term[parserStack[-1]], inputStack[-1]):
                stackMatch()
            else:
                Data[-1][-1] = 'Reject!!'
                reject = True
                break;
        elif isinstance(nonTerm[parserStack[-1]], str):
            string = nonTerm[parserStack[-1]].split(' ')
            string.reverse()
            Data[-1][-1] = 'Predict: {key} --> {value}'.format(key = parserStack[-1], value = nonTerm[parserStack[-1]])
            parserStack.pop()
            for letter in string:
                parserStack.append(letter)
            Data = np.append(Data, [parserStack, inputStack, 'a'])
            i += 1
        else:
            choice = decider(parserStack[-1], inputStack[-1])
            if choice == -1:
                Data[-1][-1] = 'Predict: {} --> λ'.format(parserStack[-1])
                parserStack.pop()
                Data = np.append(Data, [parserStack, inputStack, 'a'])
                i += 1
            elif choice == -2:
                Data[-1][-1] = 'Reject!!'
                reject = True
                break;
            else:
                string = nonTerm[parserStack[-1]][choice].split(' ')
                string.reverse()
                Data[-1][-1] = 'Predict: {key} --> {value}'.format(key = parserStack[-1], value = nonTerm[parserStack[-1]][choice])
                parserStack.pop()
                for letter in string:
                    parserStack.append(letter)
                Data = np.append(Data, [parserStack, inputStack, 'a'])
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
            if choice == -1 or choice == -2:
                return False
            else:
                return True

def mapping():
    global Data, i
    Data.shape = (i, 3)
    table = tabulate(Data, headers=['parser Stack', 'input Stack', 'Action'])
    return table
