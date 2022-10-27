from pprint import pprint
from loguru import logger
from lexer import Lexer

if __name__ == '__main__':
    while True:
        text = input()
        lex = Lexer(text)
        tokens = lex.generate_tokens()
        pprint(tokens)
