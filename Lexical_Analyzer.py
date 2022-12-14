import numpy as np
from tabulate import tabulate  # table the data
import nltk
import CFG

class LAnltk:
    def __init__(self, url):
        f = open(url)
        self.tokens = nltk.wordpunct_tokenize(f.read())
        #print(self.tokens)
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
        tags = CFG.tokensTag()
        for token in self.tokens:
            data = np.append(data, [token, tags.getType(token)])
            rows += 1
        data.shape = (rows, 2)
        table = tabulate(data, headers=['Lexeme', 'Token'])
        return table
