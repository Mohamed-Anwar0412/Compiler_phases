import numpy as np
from tabulate import tabulate
import nltk
import CFG


class LexicalAnalyzer:
    def __init__(self, url):
        f = open(url)
        self.tokens = nltk.wordpunct_tokenize(f.read())
        f.close()
        for i in range(len(self.tokens)):
            if self.tokens[i] == '++;':
                self.tokens[i] = '++'
                self.tokens.insert(i + 1, ';')
            elif self.tokens[i] == '--;':
                self.tokens[i] = '--'
                self.tokens.insert(i + 1, ';')

    def mapping(self):
        data = []
        rows = 0
        tags = CFG.TokenTag()
        for token in self.tokens:
            data = np.append(data, [token, tags.get_type(token)])
            rows += 1
        data.shape = (rows, 2)
        table = tabulate(data, headers=['Lexeme', 'Token'])
        return table
