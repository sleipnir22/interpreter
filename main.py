from lexer import Token
from parser import Parser, ExpressionSyntax, SyntaxNode
from syntax_tree import SyntaxTree


def pretty_print(node: SyntaxNode, indent='', is_last=True):
    marker = "└──" if is_last else "├──"
    print(indent, end='')
    print(marker, end='')
    print(node.token_type, end='')

    if isinstance(node, Token):
        print(" ", end='')
        print(node.value, end='')

    print()
    indent += "    " if is_last else "│   "

    if not isinstance(node, Token):
        *_, last_child = node.get_children()

        for child in node.get_children():
            pretty_print(child, indent, child == last_child)

def some_func():
    yield True
    yield False
    yield 1


if __name__ == '__main__':
    while True:
        text = input()
        parser = Parser(text)
        parsed_text = parser.parse()
        something = some_func()
        pretty_print(parsed_text.root)
        pass
