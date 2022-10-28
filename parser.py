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


class CommandExpressionSyntax(ExpressionSyntax):
    command_op: Token
    id_token: Token
    value: Token
    image: Token
    token_type = TokenType.COMMAND


class Parser:
    def __init__(self, text):
        lex = Lexer(text)
        self.current_token = None
        self.tokens = iter(lex.generate_tokens())
        self.pos = 0
        self.advance()

    def advance(self) -> Token:
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
        expr = self.parse_command_expr()

    def next_token(self):
        pass

    def parse_command_expr(self):
        command = self.parse_command()

    def parse_command(self):
        if self.current_token.type == TokenType.COMMAND:
            pass

    def factor(self):
        pass