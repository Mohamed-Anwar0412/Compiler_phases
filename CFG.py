
class CFG:
    def __init__(self):
        self.NonTerm = {'S': 'if(cond){stat}T',
                    'T': ['else{stat}', ''],
                    'cond': 'id cop id Cd',
                    'Cd': ['&& cond Cd', '|| cond Cd', ''],
                    'id': ['letter', 'digit'],
                    'stat': 'letter = calc;',
                    'calc': 'id D',
                    'D': ['opH id calcD', 'calcD'],
                    'calcD': ['op calc calcD', '']}


        self.Term = {'cop': r'<|>|(<=)|(>=)|(==)|&|[|]',
                     'letter': r'[a-zA-Z_]+[a-zA-Z0-9_]*',
                     'digit': r'[0-9]*',
                     'opH': r'[*]|/|%|\\|[\^]|[+]|-',
                     'op': r'[+]|-'}
