import sys

from core.parser import parser

filename = sys.argv[1]

with open(filename, "r") as file:
    content = file.read() + "\n"

    lexer = parser(content)
    lexer.parse()