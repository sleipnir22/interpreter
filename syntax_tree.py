from lexer import Token

class SyntaxTree:
    def __init__(self, root, eof_token: Token):
        self.root = root
        self.eof_token = eof_token

