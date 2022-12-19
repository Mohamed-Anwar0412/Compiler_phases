import nltk
from Syntax_Analyzer import *

parseTreeFormat = []
tokens = []
synTree = []
listOfTres = []


def setSem(lx):
    global tokens
    tokens = lx.tokens


def setTree():
    global parseTreeFormat
    count = 0
    insertNode(count)
    count += 2
    while predictKeys:
        if parseTreeFormat[count] == predictKeys[0]:
            parseTreeFormat.pop(count)
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
    global parseTreeFormat
    for item in list:
        parseTreeFormat.insert(index, item)
        index += 1


def ToString(list):
    strTree = ''
    for item in list:
        strTree += item + ' '
    return strTree



def getSegments():
    global listOfTres
    string = ToString(tokens)
    condition = re.findall(r"\(.*?\)", string)[0]
    condition = condition.strip('( ')
    condition = condition.strip(' )')
    listOfTres.append(condition + ';')

    body=re.findall(r"{.*?}", string)
    for i in range(len(body)):
        body[i] = body[i].strip('{ ')
        body[i] = body[i].strip(' }')
        listOfTres.append(body[i])


def setMainBranch():
    global synTree, listOfTres
    if len(listOfTres) == 3:
        synTree = ['[ ', 'if ',
                        '[ ', 'Condition ', binaryTree(listOfTres[0]) + ' ', ']',
                        '[ ', 'Body ', binaryTree(listOfTres[1]) + ' ', ']',
                        '[ ', 'else ', binaryTree(listOfTres[2]) + ' ', ']',
                   ']']
    else:
        synTree = ['[ ', 'if ',
                        '[ ', 'Condition ', binaryTree(listOfTres[0]) + ' ', ']',
                        '[ ', 'Body ', binaryTree(listOfTres[1]) + ' ', ']',
                   ']']


def binaryTree(string):
    statements = string.split(';')[:-1]
    tree = ''
    for stat in statements:
        tokens = stat.split(' ')
        for item in tokens:
            if item == '':
                tokens.remove(item)
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
    if not tokens:
        return ''
    return tokens[0]

def DrawTree(choice):
    if choice == 1:
        setTree()
        #print(ToString(parseTreeFormat))
        t = nltk.Tree.fromstring(ToString(parseTreeFormat), brackets='[]')
        print(t.draw())
    elif choice == 2:
        getSegments()
        setMainBranch()
        #print(ToString(synTree))
        t = nltk.Tree.fromstring(ToString(synTree), brackets='[]')
        print(t.draw())
    else:
        DrawTree(1)
        DrawTree(2)
