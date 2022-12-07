import tokenize as tn
import numpy as np
from tabulate import tabulate  # table the data
import nltk

class LexicalAnalyzer:

    def __init__(self, url):
        f = tn.open(url)
        self.tokens = tn.generate_tokens(f.readline)
        #print(self.tokens)
        self.tokens = [token for token in self.tokens if tn.tok_name[token.type] != 'NEWLINE' and tn.tok_name[token.type] != 'ENDMARKER' and tn.tok_name[token.type] != 'NL']
        #print(self.tokens)
        for token in self.tokens:
            print(token.string, tn.tok_name[token.exact_type])

    def mapping(self):
        data = []
        i = 0
        for token in self.tokens:
            i += 1
            data = np.append(data, [token.string, tn.tok_name[token.exact_type]])
        data.shape = (i, 2)
        table = tabulate(data, headers=['Lexeme', 'Token'])
        return table

class LAnltk:
    def __init__(self):
        f = open('test.txt')
        st = f.read()
        self.tokens = nltk.word_tokenize(st)
        print(self.tokens)
