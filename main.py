import Lexical_Analyzer as lX
import CFG
import Semantic_Analyzer as Sem
import Syntax_Analyzer as sA
import ast
import nltk


URL = 'test.txt'

nltkLA = lX.LAnltk(URL)

#print(nltkLA.mapping())

cfg_rules = CFG.CFG()
sA.setParser(nltkLA, cfg_rules)
sA.LLparser()
print(sA.mapping())
#print(sA.predictKeys)
#print(sA.predictValues)

Sem.setSem(nltkLA, cfg_rules)


Sem.setTree()
#print(Sem.treeFormat)

t = nltk.Tree.fromstring(Sem.setTreeformat(), brackets='[]')



# st = nltk.Tree.fromstring(Sem.setSynTree(), brackets='[]')

print(t.draw())
# print(st.draw())

#semantic = Sem.Semantic_Analyzer(cfg_rules, nltkLA)

#print(Sem.getFromString(sA.predict_stack))


# string = "if(x>=Y) {y++;}"
# Semantic_Analyzer.Semantic_Analyzer(string)



outputURL = 'out.txt'
with open(outputURL, 'w', encoding='utf-8') as f:
    f.write(sA.mapping())
    f.close()

