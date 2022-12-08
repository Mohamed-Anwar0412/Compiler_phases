import Lexical_Analyzer as lX
import CFG
import Semantic_Analyzer
import Syntax_Analyzer as sA


URL = 'test.txt'

nltkLA = lX.LAnltk(URL)

print(nltkLA.mapping())

cfg_rules = CFG.CFG()
sA.setParser(nltkLA, cfg_rules)
sA.LLparser()
print(sA.mapping())

outputURL = 'out.txt'

with open(outputURL, 'w', encoding='utf-8') as f:
    f.write(sA.mapping())
    f.close()

