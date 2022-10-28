from abc import ABC, abstractmethod
from enum import Enum
from typing import Iterable, TypeVar

from pydantic import BaseModel

from lexer import TokenType, Token, Lexer


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


class Parser:
    def __init__(self, text):
        lex = Lexer(text)
        tokens = lex.generate_tokens()

    def parse(self):
        expr = self.term()

    def next_token(self):
        pass

    def term(self):
        pass

    def factor(self):
        pass