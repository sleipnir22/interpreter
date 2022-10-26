from abc import ABC, abstractmethod
from typing import Iterable, TypeVar


class SyntaxNode(ABC):
    def __init__(self, token_type):
        self.token_type = token_type

    @abstractmethod
    def get_children(self) -> Iterable['SyntaxNode']:
        ...


class ExpressionSyntax(SyntaxNode):
    pass


class BinaryExpressionSyntax(SyntaxNode):
    pass

class Parser:
    pass