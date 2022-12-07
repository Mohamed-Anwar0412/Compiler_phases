import ast
class semantic:
    def __init__(self, exp):
        node = ast.parse(exp, mode="eval")
        dump = ast.dump(node)

        print(dump)