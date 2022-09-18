with open("testing/main.cb", "r") as file:
    string = file.read()

    i = 0

    while i != len(string):
        print(string[i] == "\n")
        i+=1