import re


class CFG:

    def __init__(self):
        self.NonTerm = {
            'S': 'if ( cond ) { stat } T',
            'T': ['else { stat }', ''],
            'cond': 'id cop id Cd',
            'Cd': ['&& cond Cd', '|| cond Cd', ''],
            'id': ['letter', 'digit', 'unF letter', '- digit'],
            'stat': ['letter L', 'unB letter ; statD'],
            'L': ['eqop calc ; statD', 'unB ; statD'],
            'statD': ['stat', ''],
            'calc': ['id D', 'V'],
            'D': ['op V', ''],
            'V': 'F VD',
            'VD': ['opH F VD', ''],
            'F': ['id', '( calc )']
        }

        self.Regex = {
            'cop': r'!=|<=|>=|==|<|>|&|[|]',
            'letter': r'[a-zA-Z_]+[a-zA-Z0-9_]*',
            'digit': r'[0-9]+',
            'opH': r'[*]|/|%|\\|\^',
            'op': r'[+]|-',
            'unF': r'--|!|\+\+|-|&|[*]',
            'unB': r'--|\+\+',
            'eqop': r'=|\+=|-=|\*=|/='
        }


class TokenTag:

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
            'ORed': r'\|\|',
            'Increment': r'\+\+',
            'Decrement': r'--',
            'compound assignment': r'=|\+=|-=|\*=|/='

        }

    def get_type(self, token):
        for key, value in self.types.items():
            if re.fullmatch(value, token):
                return key
        return 'Unknown'
