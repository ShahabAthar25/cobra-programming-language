from Core.Interpreter import Interpreter
from Core.Lexer import Lexer
from Core.Parser import Parser


while True:
    try:
        text = input("COBRA >>> ")

        lexer = Lexer(text)
        tokens = lexer.generate_tokens()

        parser = Parser(tokens)
        tree = parser.parse()

        if not tree: continue

        interpreter = Interpreter()
        value = interpreter.visit(tree)

        print(value)
    except Exception as error:
        print(error)