from lexer import Lexer

def run(text):
    lexer = Lexer(text)
    tokens, error = lexer.make_tokens()

    return tokens, error

while True:
    try:
        text = input("COBRA >>> ")
        result, error = run(text)

        if error: print(error.as_string())
        else: print(result)
    except KeyboardInterrupt:
        print("\n", end="")
        break
    except Exception as e:
        print("Error: ", e)