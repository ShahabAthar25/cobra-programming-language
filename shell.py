from Core.Lexer import Lexer
from Core.Parser import Parser


while True:
    text = input("COBRA >>> ")

    lexer = Lexer(text)
    tokens = lexer.generate_tokens()

    parser = Parser(tokens)
    tree = parser.parse()

    print(tree)