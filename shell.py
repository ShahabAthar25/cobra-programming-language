from core.Lexer import Lexer


while True:
    text = input("COBRA >>> ")

    lexer = Lexer(text)
    tokens = lexer.generate_tokens()

    print(list(tokens))