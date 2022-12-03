import Lexical_Analyzer as lX
import CFG
import Syntax_Analyzer as sA
import re

URL = 'test.txt'

_lexAnalyzer = lX.LexicalAnalyzer(URL)
cfg_rules = CFG.CFG()
_syntaxAnalyzer = sA.SyntaxAnalyzer(_lexAnalyzer, cfg_rules)
#print(cfg1.cfg)

print(_syntaxAnalyzer.tokens)
print(_syntaxAnalyzer.nonterm)
print(_syntaxAnalyzer.term)


# if cfg_rules.match('op', r'\\'):
#     print('nice')
# else:
#     print('a7a')


#print(_lexAnalyzer.mapping())
