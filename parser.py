from abc import ABC, abstractmethod
from typing import Iterable

from pydantic import BaseModel

from lexer import TokenType, Token, Lexer
from syntax_tree import SyntaxTree


class SyntaxNode(ABC, BaseModel):
    token_type: TokenType

    @abstractmethod
    def get_children(self) -> Iterable['SyntaxNode']:
        ...


class ExpressionSyntax(SyntaxNode):
    pass


class NumberExpressionSyntax(ExpressionSyntax):
    number_token: Token
    token_type = TokenType.NUMBER

    def get_children(self) -> Iterable[SyntaxNode]:
        yield self.number_token


class BinaryExpressionSyntax(ExpressionSyntax):
    left: ExpressionSyntax
    operator: Token
    right: ExpressionSyntax
    token_type = TokenType.OPERATOR

    def get_children(self) -> Iterable[SyntaxNode]:
        yield self.left
        yield self.operator
        yield self.right


class ParenthesizedExpressionSyntax(ExpressionSyntax):
    lpar_token: Token
    expression: ExpressionSyntax
    rpar_token: Token
    token_type = TokenType.PARENEXPR

    def get_children(self) -> Iterable[SyntaxNode]:
        yield self.lpar_token
        yield self.expression
        yield self.rpar_token


class CommandExpressionSyntax(ExpressionSyntax):
    command_op: Token
    id_token: Token
    value: Token
    image: Token
    token_type = TokenType.COMMAND


class Parser:
    def __init__(self, text):
        lex = Lexer(text)
        self.current_token: Token = Token()
        self.tokens = iter(lex.generate_tokens())
        self.pos = 0
        self.advance()

    def advance(self):
        try:
            self.pos += 1
            self.current_token = next(self.tokens)
        except StopIteration as e:
            self.current_token = Token(
                value=None,
                type=TokenType.BADTOKEN,
                pos=self.pos
            )
        return self.current_token

    def parse(self):
        expr = self.term()
        eof_token = self.match(TokenType.EOF)
        return SyntaxTree(expr, eof_token)

    def term(self) -> ExpressionSyntax:
        left = self.factor()
        while self.current_token.token_type in (TokenType.PLUS, TokenType.MINUS):
            operator_token = self.advance()
            right = self.factor()
            left = BinaryExpressionSyntax(left, operator_token, right)

        return left

    def factor(self) -> ExpressionSyntax:
        left = self.primary_expression()
        while self.current_token.token_type in (TokenType.MULTIPLICATION, TokenType.DIVISION):
            operator_token = self.advance()
            right = self.primary_expression()
            left = BinaryExpressionSyntax(left, operator_token, right)

        return left

    def primary_expression(self):
        if self.current_token.token_type == TokenType.LPAREN:
            left = self.advance()

            expression = self.expression()

            right = self.match(TokenType.RPAREN)
            return ParenthesizedExpressionSyntax(left, expression, right)

        number_token = self.match(TokenType.NUMBER)
        return NumberExpressionSyntax(number_token=number_token)

    def expression(self):
        return self.term()

    def match(self, token_type: TokenType):
        if self.current_token.token_type == token_type:
            return self.advance()
        else:
            #BAD TOKEN!!! Exception
            pass

