from lexer import TokenType
from parser import ExpressionSyntax, NumberExpressionSyntax, BinaryExpressionSyntax, ParenthesizedExpressionSyntax


class Interpreter:
    def __init__(self, root: ExpressionSyntax):
        self.root = root

    def interprete(self):
        return self._interprete_expression(self.root)

    def _interprete_expression(self, node: ExpressionSyntax):
        if isinstance(node, NumberExpressionSyntax):
            return int(node.number_token.value)

        if isinstance(node, BinaryExpressionSyntax):
            left = self._interprete_expression(node.left)
            right = self._interprete_expression(node.right)

            if node.operator.token_type == TokenType.PLUS:
                return left + right
            elif node.operator.token_type == TokenType.MINUS:
                return left - right
            elif node.operator.token_type == TokenType.MULTIPLICATION:
                return left * right
            elif node.operator.token_type == TokenType.DIVISION:
                return left / right
            else:
                raise Exception(f'Unexpected binary operator {node.operator.token_type}')

        if isinstance(node, ParenthesizedExpressionSyntax):
            return self._interprete_expression(node.expression)

        raise Exception(f'Unexpected binary operator {node.token_type}')


