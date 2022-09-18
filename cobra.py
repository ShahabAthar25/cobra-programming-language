import sys

from core.lexer import lexer

file_name = sys.argv[1]

try:
    with open(file_name, "r") as file:
        content = file.read()

        lx = lexer(content)
        lx.commit()
        print(lx.get_tree())
except FileNotFoundError:
    print(f"No file exist with path of ${file_name}")