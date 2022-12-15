import nltk
from Syntax_Analyzer import *


treeFormat = []
tokens = []
nonTerm = []
term = []
inputstring = ''

synTree = []

listOfTres = []


def setSem(lX, cfg):
    global tokens, nonTerm, term
    tokens  = lX.tokens
    nonTerm = cfg.NonTerm
    term = cfg.Term



def setTree():
    global treeFormat
    count = 0
    while predictKeys:
        if not treeFormat:
            insertNode(count)
            count += 2
        else:
            if treeFormat[count] == predictKeys[0]:
                treeFormat.pop(count)
                insertNode(count)
                count += 2
            else:
                count += 1

def insertNode(index):
    insertValue(['[', predictKeys.pop(0)], index)
    index += 2
    value = predictValues.pop(0).split(' ')
    value.append(']')
    insertValue(value, index)

def insertValue(list, index):
    global treeFormat
    for item in list:
        treeFormat.insert(index, item)
        index += 1

def setTreeformat():
    strTree = ''
    for item in treeFormat:
        strTree += item + ' '
    return strTree

def setSynTree():
    strTree = ''
    print(nonTerm)
    print(term)
    buffer = ''
    for item in treeFormat:
        if item in [key for key in nonTerm] or item in [key for key in term] or item in ['(', ')', '{', '}']:
            buffer = item
            continue
        elif item == ']' and buffer == '[':
            strTree = strTree[:-2]
        else:
            # strTree += item + ' '
            strTree += item
            buffer = item
        print(strTree)
    return strTree
def sharkway():
    global inputstring
    for item in tokens:
        inputstring += item + ' '



def getSegments():
    global inputstring, listOfTres
    sharkway()
    condition = re.findall(r"\(.*?\)",inputstring)[0]
    condition = condition.strip('( ')
    condition = condition.strip(' )')
    listOfTres.append(condition + ';')

    body=re.findall(r"{.*?\}",inputstring)
    for i in range(len(body)):
        body[i] = body[i].strip('{ ')
        body[i] = body[i].strip(' }')
        listOfTres.append(body[i])
    print(listOfTres)


def setMainBranch():
    global synTree, listOfTres
    if len(listOfTres) == 3:
        synTree = ['[ ', 'if ', '[ ', 'Condition ', binaryTree(listOfTres[0]) + ' ', ']', '[ ', 'Body ', binaryTree(listOfTres[1]) + ' ', ']', '[ ', 'else ', binaryTree(listOfTres[2]) + ' ', ']', ']']
    else:
        synTree = ['[ ', 'if ', '[ ', 'Condition ', binaryTree(listOfTres[0]) + ' ', ']', '[ ', 'Body ', binaryTree(listOfTres[1]) + ' ', ']', ']']


def binaryTree(string):
    statements = string.split(';')[:-1]
    tree = ''
    print(statements)
    for stat in statements:
        tokens = stat.split(' ')
        for item in tokens:
            if item == '':
                tokens.remove(item)
        print(tokens)
        tree += '[ ' + tokens[1] + ' ' + tokens[0] + ' ' + setBranch(tokens[2:]) + ' ]'
    return tree



def setBranch(tokens):
    node = ''
    for token in tokens:
        if re.match(r'[+]|-', token):
            node += '[ ' + token + ' ' + setBranch(tokens[:tokens.index(token)]) + ' ' + setBranch(tokens[tokens.index(token) + 1:]) + ' ]'
            return node
    for token in tokens:
        if re.match(r'[*]|/|%|\\|\^', token):
            node += '[ ' + token + ' ' + setBranch(tokens[:tokens.index(token)]) + ' ' + setBranch(tokens[tokens.index(token) + 1:]) + ' ]'
            return node
    print(tokens)
    if not tokens:
        return ''
    return tokens[0]

def setSynTreeformat():
    strTree = ''
    for item in synTree:
        strTree += item + ' '
    return strTree

