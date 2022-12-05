import Lexical_Analyzer as lX
import CFG
import Syntax_Analyzer as sA
import re
import ply.yacc as yacc
import nltk
#nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('treebank')

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
sA.LLparser()
sA.mapping()
string = ['sdf', 'asdfas', 'sadf']
string.reverse()
print(string)
#print(cfg1.cfg)

# print(sA.tokens)
# print(sA.nonTerm)
# print(sA.term)

#sA.LLparser()

# if cfg_rules.match('op', r'\\'):
#     print('nice')
# else:
#     print('a7a')


# #print(_lexAnalyzer.mapping())
# f = open(URL)
# st = f.read()
# print(st)
# tokens = nltk.word_tokenize(st)
# print(tokens)
#
# tagged = nltk.pos_tag(tokens)
# print(tagged)
#
# entities = nltk.chunk.ne_chunk(tagged)
# print(entities)
# # chunker = nltk.RegexpParser()
# # from nltk.corpus import treebank
# # t = treebank.parsed_sents(tokens)[0]
# # t.draw()
# nonterminals = [key for key in cfg_rules.NonTerm]
# combinded = ''
# for i in nonterminals:
#     combinded += i
#     combinded +=' '
# # combinded = combinded[:-2]
# print(combinded)
# nltk.grammar.ter
# print(nltk.grammar.nonterminals(combinded))

# if isinstance(cfg_rules.NonTerm['T'], list):
#     print('sdf')
# print(sA.nt_Decider('T', 's'))