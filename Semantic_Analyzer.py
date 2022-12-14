import nltk
from nltk.draw.util import TextWidget
from pptree import *
from Syntax_Analyzer import *
from baron import *
from baron.helpers import *
import ast
#from treelib import Node, Tree

treeFormat = []
tokens = []
nonTerm = []
term = []
# childrenStack = []
# father = None
# tree = Tree()
# count = 1


def setSem(lX, cfg):
    global tokens, nonTerm, term
    tokens  = lX.tokens
    nonTerm = cfg.NonTerm
    term = cfg.Term


# # for key, value in cfg.NonTerm.items():
# #     string += '{} -> {}\n'.format(key, value)
grammer = nltk.CFG.fromstring(r"""
    S -> 'if' '(' cond ')' '{' stat '}' T
    T -> 'else' '{' stat '}' | ''
    cond -> id cop id Cd
    Cd ->'&&' cond Cd | '||' cond Cd | ''
    id ->'letter' | 'digit' | 'unF' 'letter'| '-' 'digit'
    stat ->'letter' L | 'unB' 'letter' ';' statD
    L -> 'eqop' calc ';' statD | 'unB' ';' statD
    statD -> stat | ''
    calc -> id D | V
    D -> 'op' V | ''
    V -> F VD
    VD -> 'opH' F VD | ''
    F -> 'id' | '(' calc ')'
    cop -> '!=' | '<=' | '>=' | '==' | '<' | '>' | '&' | '[|]'
    letter -> 'x' | 'y'
    digit -> '0' | '3' | '4' | '5' | '6'
    opH -> '[*]' | '/' |'%' | '\\' | '^'
    op -> '+' | '-'
    unF -> '--' | '!' | '++' |'-' | '&' | '[*]'
    unB -> '--' | '++'
    eqop -> '=' | '+=' | '-=' | '*=' | '/='
""")


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


# self.tree = parseTree()
# print_tree(self.tree, horizontal=False)

# parser = nltk.ChartParser(grammer)
# trees = list(parser.parse(lX.tokens))
# print(trees)
# parseTree()
# tree.show()
# grammer.productions()
# print(grammer.productions())
#
# sent = lX.tokens
# parser = nltk.ChartParser(grammer)
# trees =list(parser.parse(sent))
# nltk.tree.pretty_print()

# def getFromString():
#     father = None
#     for key, value in sA.predict_stack.items():
#         setBranch(key, father)
#
# def setBranch(key, father):
#     parseTree.append(Node(key, father))
#     list = sA.parserStack[key].split(' ')
#     for item in list:
#         parseTree.append(item, key)
#         if item in sA.predict_stack.keys():
#             getFromString(item, key)

#
# def parseTree():
#     father = Node(predictKeys[0])
#     setBranch(father)
#     return father
#
# def setBranch(father):
#     predictKeys.pop(0)
#     children = predictValues.pop(0).split(' ')
#     for child in children:
#         cnode = Node(child, father)
#         if predictKeys != [] and child == predictKeys[0]:
#             setBranch(cnode)


# def parseTree():
#     global tree
#     tree.create_node(predictKeys[0], 1)
#     setBranch(1)
#     return father
#
# def setBranch(index):
#     global tree, count
#     predictKeys.pop(0)
#     children = predictValues.pop(0).split(' ')
#     for child in children:
#         count += 1
#         tree.create_node(child, count, parent=index)
#         if predictKeys != [] and child == predictKeys[0]:
#             setBranch(count)

