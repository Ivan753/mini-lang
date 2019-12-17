"""
Parser which works with tokens
"""
import sys

from lexer import Lexer, TokenType


class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def match(self, expectedTypes):
        if self.pos < len(self.tokens):
            token = self.tokens[self.pos]
            if token.type in expectedTypes:
                self.pos += 1
                return True

        return False

    def expr(self):
        e1 = self.slag()
        while self.match([TokenType.ADD, TokenType.SUB]):
            op = self.tokens[self.pos-1]
            e2 = self.slag()
            e1 = BinOpNode(op.text, e1, e2)

        return e1

    def logic_expr(self):
        e1 = self.expr()
        while self.match([TokenType.MORE, TokenType.LESS, TokenType.EMORE, TokenType.ELESS]):
            op = self.tokens[self.pos-1]
            e2 = self.expr()
            e1 = BinOpNode(op.text, e1, e2)

        return e1

    def statement(self):
        list = []

        while self.match([TokenType.PRINT, TokenType.ID, TokenType.IF]):
            statement = self.tokens[self.pos-1]

            if statement.type == TokenType.PRINT:
                expr = self.expr()

                node = StatementNode(statement, expr)
            elif statement.type == TokenType.ID:
                self.require([TokenType.ASSIGN])
                expr = self.expr()

                node = StatementNode(statement, expr)
            elif statement.type == TokenType.IF:
                expr = self.logic_expr()
                self.require([TokenType.THEN])

                node = StatementNode(statement, expr)
                node.s_then = self.statement()

                if self.match([TokenType.ELSE]):
                    node.s_else = self.statement()

                self.require([TokenType.END])

            list.append(node)

            self.require([TokenType.SEMICOLON])

        return list

    def mnog(self):
        if self.match([TokenType.LPAR]):
            e = self.expr()
            self.require([TokenType.RPAR])
            return e
        else:
            e = self.require([TokenType.NUMBER, TokenType.ID])
            if e.type == TokenType.ID:
                e = VarNode(e.text)
            else:
                e = NumberNode(e.text)
            return e

    def slag(self):
        e1 = self.mnog()
        while self.match([TokenType.MUL, TokenType.DIV]):
            op = self.tokens[self.pos-1]
            e2 = self.mnog()

            e1 = BinOpNode(op.text, e1, e2)

        return e1

    def require(self, expecteds):
        if not self.match(expecteds):

            if not isinstance(expecteds[0].value, str):
                value = expecteds[0].value[0]
            else:
                value = expecteds[0].value
            self.error("Ожидалось {}".format(value))
        return self.tokens[self.pos-1]

    def error(self, msg):
        print(self.tokens[self.pos-1].text)
        raise Exception(
            "{} в строке {} на позиции {}"
                .format(
                    msg, self.tokens[self.pos-1].line+1,
                    len(self.tokens[self.pos-1].text)+self.tokens[self.pos-1].pos_in_line-1
                )
            )

    def runtime_error(self, msg):
        raise Exception(msg)

# элементы AST

class NumberNode:
    #number;
    def __init__(self, number):
        self.number = number

class VarNode:
    #id
    def __init__(self, var):
        self.var = var

class BinOpNode:
    #op
    #left
    #right
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

class StatementNode:
    #statement;
    def __init__(self, statement, ast):
        self.statement = statement
        self.expr = ast
        self.s_then = []
        self.s_else = []

    def append(self, statement):
        self.list.append(statement)
