import nltk
from nltk.draw.util import TextWidget
class Semantic_Analyzer:
    def __init__(self, cfg, lX):
        # string = ''
        # for key, value in cfg.NonTerm.items():
        #     string += '{} -> {}\n'.format(key, value)
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
        # grammer.productions()
        # print(grammer.productions())
        #
        # sent = lX.tokens
        # parser = nltk.ChartParser(grammer)
        # trees =list(parser.parse(sent))
        # nltk.tree.pretty_print()

def getFromString(predictList):
    fromString = 'S'
    string = fromString.split(' ')
    while predictList:
        for i in range(len(string)):
            if string[i] in [key for key in predictList]:
                predictList.pop(string[i])
                node = '[ {} {} ]'.format(string[i], predictList[string[i]])
                string[i] = node.split(' ')
    return string

