print("Cobra 0.0.1 Shell")
print("Type help() for help")

while True:
    try:
        command = input(">>> ")

        if command == "exit":
            break
    except KeyboardInterrupt:
        print("\nPlease type exit or press ctrl+d")
    except:
        print("\nExiting Cobra shell")
        print("Goodbye!!!")
        break
