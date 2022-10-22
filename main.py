import ast
from lexer import Lexer
from parser import Parser

def run(fn, text):
    # Generating tokesn
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()
    if error: return None, error

    # Generating AST
    parser = Parser(tokens)
    ast = parser.parse()

    return ast, error

while True:
    try:
        text = input("COBRA >>> ")
        result, error = run('<stdin>', text)

        if error: print(error.as_string())
        else: print(result)
    except KeyboardInterrupt:
        print("\n", end="")
        break
    # except Exception as e:
    #     print("Error: ", e)