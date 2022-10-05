from core.functions.printLn import printLn


class Executer:
    def __init__(self, tree) -> None:
        self.tokens = tree

    def match_values(self, value1, value2):
        return value1.get("name") == value2

    def execute(self):
        for i in range(len(self.tokens)):
            current_token = self.tokens[i]

            if self.match_values(current_token, "printLn"):
                printLn(current_token)