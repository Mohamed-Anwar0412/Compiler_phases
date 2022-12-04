import Lexical_Analyzer as lX
import CFG
import Syntax_Analyzer as sA
import re

URL = 'test.txt'

# test = 'cf sd da'
# print(test)
#
# test = test.split(' ')
# print(test)
# temp = ''
# for par in test:
#     temp += par
#     temp += ' '
# test = temp
# print(test)

_lexAnalyzer = lX.LexicalAnalyzer(URL)
cfg_rules = CFG.CFG()
sA.setParser(_lexAnalyzer,cfg_rules)
#print(cfg1.cfg)

# print(sA.tokens)
# print(sA.nonTerm)
# print(sA.term)

#sA.LLparser()

# if cfg_rules.match('op', r'\\'):
#     print('nice')
# else:
#     print('a7a')


#print(_lexAnalyzer.mapping())
