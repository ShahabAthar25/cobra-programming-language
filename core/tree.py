class tree:
    def __init__(self):
        self.version = "0.0.1"
        self.tree = []
        self.ch = 0

    def throw_error(self, error, i=0):
        if error == "syntax":
            line = self.line.split("\n")
            print(f"Systax Error at line {self.line_no + 1} and charecter {i}")
            spaces = ""
            for x in range(i):
                spaces = spaces + " "
            print(f"|\n| {line[self.line_no]} <-- Syntax error\n| {spaces}^")
            print(f"Error Type: {error}")
        elif error == "unhandled_error":
            print("Unhandled error!!!")
            print("    This is likely a problem with the current version of cobra. please report it.")
            print(f"\n   This error occured because cobra {self.version} issued a error which was not handled and cobra didn't know how to deal with it. This not a problem with your program but with cobra. Please report it so we can make a better language for everyone and for you to continue with your journey")
            print(f"Error Type: {error}")

        exit()

    def tree_add_item(self, type, name, values, extras=[]):
        if (type == "inline_func"):
            self.tree.append({
                "type": type,
                "name": name,
                "values": values,
                "extras": extras
            })
        else:
            self.throw_error("unhandled_error")

    def get_tree(self):
        return self.tree