import tokenize as tn
import re

reject = False
tokens = []
nonTerm =[]
term = []
inputStack =[]
parserStack = ['S']

def setParser(lX, cfg):
    global tokens, nonTerm, term, inputStack
    tokens = lX.tokens
    nonTerm = cfg.NonTerm
    term = cfg.Term
    for token in tokens:
        inputStack.append(token.string)
    print(inputStack)
    #inputStack.reverse()


    # def match(self, key, s):
    #     return re.match(self.Term[key], s)

def LLparser():
    global reject
    while True:
        if inputStack == [] and parserStack == []:
            break;
        if parserStack[0] in [key for key in term]:
            if re.match(term[parserStack[0]], inputStack[-1]):
                inputStack.pop(0)
                parserStack.pop(0)
            else:
                reject = True
                break



