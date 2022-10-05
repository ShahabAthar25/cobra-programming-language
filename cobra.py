import sys
from core.executer import Executer

from core.parser import parser

filename = sys.argv[1]

with open(filename, "r") as file:
    content = file.read() + "\n"

    lexer = parser(content)
    lexer.parse()

    tree = lexer.get_tree()

    tokens = Executer(tree)
    tokens.execute()

    