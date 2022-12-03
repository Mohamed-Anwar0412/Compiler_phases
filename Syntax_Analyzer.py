import re

class SyntaxAnalyzer:
    def __init__(self, lX, cfg):
        self.tokens = lX.tokens
        self.nonterm = cfg.NonTerm
        self.term = cfg.Term

    def match(self, key, s):
        return re.match(self.Term[key], s)

