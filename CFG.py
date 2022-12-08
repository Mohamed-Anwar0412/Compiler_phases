import re


class CFG:
    def __init__(self):
        self.NonTerm = {
            'S': 'if ( cond ) { stat } T',
            'T': ['else { stat }', ''],
            'cond': 'id cop id Cd',
            'Cd': ['&& cond Cd', '|| cond Cd', ''],
            'id': ['letter', 'digit'],
            'stat': 'letter = calc ; statD',
            'statD': ['stat', ''],
            'calc': 'id D',
            'D': ['opH id calcD', 'calcD'],
            'calcD': ['op calc calcD', '']
        }


        self.Term = {
            'cop': r'!=|<=|>=|==|<|>|&|[|]',
            'letter': r'[a-zA-Z_]+[a-zA-Z0-9_]*',
            'digit': r'[0-9]+',
            'opH': r'[*]|/|%|\\|\^|[+]|-',
            'op': r'[+]|-'
        }

class tokensTag:
    def __init__(self):
        self.types = {
            'Keyword': r'(if)|(else)',
            'Identifier': r'[a-zA-Z_]+[a-zA-Z0-9_]*',
            'Semi-colon': r';',
            'Curly_Bracket': r'[{|}]',
            'Parentheses': r'[(|)]',
            'AssignmentOp': r'=',
            'Plus': r'[+]',
            'Minus': r'-',
            'Multiplied': r'[*]',
            'Divided': r'/',
            'Integer Division': r'\\',
            'Power': r'\^',
            'Modulus': r'%',
            'Number': r'[0-9]+',
            'Less Than': r'<',
            'Greater Than': r'>',
            'Greater Equal': r'>=',
            'Less Equal': r'<=',
            'Is Equal': r'==',
            'Not Equal': r'!=',
            'AND': r'&',
            'OR': r'|',
            'ANDed': r'&&',
            'ORed': r'\|\|'
        }
    def getType(self, token):
        for key, value in self.types.items():
            if re.fullmatch(value, token):
                return key
        return 'Unknown'
