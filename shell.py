import core.Lexer as lexer

while True:
    text = input("COBRA >>> ")

    result = lexer.run(text, "<stdin>")

    print(result)