from parser import NumberNode, VarNode, BinOpNode, StatementNode
from lexer import TokenType

class Executor:

    def eval_statement(self, list, variables):
        for item in list:
            if type(item) is StatementNode: # возможно, лишнее
                # print
                if item.statement.type == TokenType.PRINT:
                    print(self.eval(item.expr, variables))

                # assign
                if item.statement.type == TokenType.ID:
                    variables[item.statement.text] = self.eval(item.expr, variables)

                # if
                if item.statement.type == TokenType.IF:
                    if self.eval(item.expr, variables):
                        self.eval_statement(item.s_then, variables)
                    else:
                        self.eval_statement(item.s_else, variables)

    def eval(self, n, variables):
        if type(n) is NumberNode:
            return int(str(n.number), 16)
        if type(n) is VarNode:
            if n.var in variables:
                return int(str(variables[n.var]), 16)
            else:
                return self.runtime_error("Неизвестная переменная " + n.var)
        if type(n) is BinOpNode:
            l = self.eval(n.left, variables)
            r = self.eval(n.right, variables)

            if n.op == '+':
                return l+r
            elif n.op == '*':
                return l*r
            elif n.op == '-':
                return l-r
            elif n.op == '/':
                return l/r
            elif n.op == '>':
                return l>r
            elif n.op == '<':
                return l<r
            elif n.op == '>=':
                return l>=r
            elif n.op == '<=':
                return l<=r
            elif n.op == '=':
                return l==r

    def runtime_error(self, msg):
        raise Exception(msg)
