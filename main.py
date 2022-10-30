from parser import Parser
from syntax_tree import SyntaxTree

if __name__ == '__main__':
    while True:
        text = input()
        parser = Parser(text)
        parsed_text = parser.parse()
        print(parsed_text)
