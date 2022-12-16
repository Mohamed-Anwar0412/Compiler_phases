import Lexical_Analyzer as lX
import CFG
import Semantic_Analyzer as Sem
import Syntax_Analyzer as sA
import os


URL = input('Enter or drop the source code here:\n')

# os.system('cls')

lA = lX.LexicalAnalyzer(URL)
print('Lexical Analyzer Output')
print(lA.mapping())

cfg_rules = CFG.CFG()

sA.setParser(lA, cfg_rules)

if sA.LLparser():
    print('Syntax Analyzer Output')
    print(sA.mapping())

    outputURL = 'out.txt'
    with open(outputURL, 'w', encoding='utf-8') as f:
        f.write(sA.mapping())
        f.close()

    choice = int(input('show 1: Parse Tree 2: Syntax Tree 3: Both: '))
    Sem.setSem(lA)
    if choice == 1:
        Sem.DrawTree(choice)
    elif choice == 2:
        Sem.DrawTree(choice)
    elif choice == 3:
        Sem.DrawTree(choice)
    else:
        print('wrong input!!')
else:
    print('Syntax Analyzer Output')
    print(sA.mapping())

    outputURL = 'out.txt'
    with open(outputURL, 'w', encoding='utf-8') as f:
        f.write(sA.mapping())
        f.close()
