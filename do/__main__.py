import sys

from lexer import Lexer
from parser import Parser
from executor import Executor

if len(sys.argv) < 2:
    raise Exception("Ожидался файл, содержащий исходный код")

with open(sys.argv[1]) as f:
    l = Lexer(f.read())

tokens = l.lex()
# for t in tokens:
    # print("value: {}, token: {}".format(t.text, t.type))

parser = Parser(tokens)
ast = parser.statement()
executor = Executor()

result = executor.eval_statement(ast, {})
