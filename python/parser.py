from py_expression_eval import Parser

def eval(fx, a):
    parser = Parser()
    return parser.evaluate(str(fx), {'x': float(a)})
