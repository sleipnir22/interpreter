from abc import ABC, abstractmethod
from enum import Enum
from typing import Iterable, TypeVar

from pydantic import BaseModel

from lexer import TokenType, Token


class SyntaxNode(ABC, BaseModel):

    token_type: TokenType
    @abstractmethod
    def get_children(self) -> Iterable['SyntaxNode']:
        ...


class ExpressionSyntax(SyntaxNode):
    pass


class NumberExpressionSyntax(ExpressionSyntax):
    number_token: Token


class BinaryExpressionSyntax(ExpressionSyntax):
    left: ExpressionSyntax
    operator: Token
    right: ExpressionSyntax
    token_type = TokenType.Operator


class Parser:
    pass