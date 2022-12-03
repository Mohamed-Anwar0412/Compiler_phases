import tokenize as tn
import numpy as np
from tabulate import tabulate  # table the data


class LexicalAnalyzer:

    def __init__(self, url):
        f = tn.open(url)
        self.tokens = tn.generate_tokens(f.readline)
        #print(self.tokens)
        self.tokens = [token for token in self.tokens if token.type != 4 and token.type != 0 and token.type != 62]
        #print(self.tokens)

    def mapping(self):
        data = []
        i = 0
        for token in self.tokens:
            i += 1
            data = np.append(data, [token.string, tn.tok_name[token.exact_type]])
        data.shape = (i, 2)
        table = tabulate(data, headers=['Lexeme', 'Token'])
        return table
