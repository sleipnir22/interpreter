from enum import Enum
import typing as t
from pydantic import BaseModel


class TokenType(str, Enum):
    CREATE = 'create'
    DELETE = 'delete'
    UPDATE = 'update'
    NUMBER = 'number'
    ID = "id"
    EXPRESSION = 'expr'
    OPERATOR = 'operator'
    WHITESPACE = 'whitespace'
    INTEGER = 'integer'
    PLUS = '+'
    MINUS = '-'
    DIVISION = '/'
    MULTIPLICATION = '*'
    LPAREN = '('
    RPAREN = ')'
    COMMA = ','
    BADTOKEN = '<error>'
    EOF = '<eof>'
    EOL = '<eol>'
    PARENEXPR = '<paren_expr>'


class Token(BaseModel):
    token_type: TokenType
    pos: int
    value: t.Any

    def __repr__(self):
        return f'[TOKEN TYPE: {self.token_type} VALUE: {self.value}]'


class Lexer:
    def __init__(self, text: str):
        self.text = iter(text)
        self.current_char = ''
        self.pos = 0
        self.tokens: list[Token] = []
        self.advance()

    def advance(self):
        try:
            self.pos += 1
            self.current_char = next(self.text)
        except StopIteration as e:
            self.current_char = None

    def generate_tokens(self) -> list[Token]:
        while self.current_char is not None:
            self.tokens.append(self.next_token())

        self.tokens.append(
            Token(
                token_type=TokenType.EOF,
                value='<eof>',
                pos=self.pos
            )
        )
        return self.tokens

    def next_token(self) -> Token:
        if self.current_char.isdigit():
            text: str = ''
            while self.current_char is not None and self.current_char.isdigit():
                text += self.current_char
                self.advance()

            num = int(text)
            return Token(
                token_type=TokenType.INTEGER,
                pos=self.pos,
                value=num
            )
        elif self.current_char.isspace():
            text: str = ''
            while self.current_char is not None and self.current_char.isspace():
                text += self.current_char
                self.advance()
            return Token(
                token_type=TokenType.WHITESPACE,
                pos=self.pos,
                value=text
            )

        elif self.current_char in ['+', '-', '/', '*', '(', ')', ',']:
            previous_char = self.current_char
            self.advance()
            return Token(
                token_type=TokenType(previous_char),
                value=previous_char,
                pos=self.pos
            )
        else:
            return Token(
                token_type=TokenType.BADTOKEN,
                value='<error>',
                pos=self.pos
            )
