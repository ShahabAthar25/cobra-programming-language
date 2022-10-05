from core.types import types


class Maths(types):
    def __init__(self):
        self.raw_expression = ""
        self.expression = {}

    def set_expression(self, expression):
        self.raw_expression = expression

    def parse_expression(self):
        if "+" in self.raw_expression:
            expression = self.raw_expression.split("+")
            self.expression = self.get_maths_obj(expression[0], "PLUS", expression[1])
        elif "-" in self.raw_expression:
            expression = self.raw_expression.split("-")
            self.expression = self.get_maths_obj(expression[0], "MINUS", expression[1])
        elif "*" in self.raw_expression:
            expression = self.raw_expression.split("*")
            self.expression = self.get_maths_obj(expression[0], "MULTIPLY", expression[1])
        elif "/" in self.raw_expression:
            expression = self.raw_expression.split("/")
            self.expression = self.get_maths_obj(expression[0], "DIVIDE", expression[1])
        elif "^" in self.raw_expression:
            expression = self.raw_expression.split("^")
            self.expression = self.get_maths_obj(expression[0], "POWER", expression[1])
        elif "%" in self.raw_expression:
            expression = self.raw_expression.split("%")
            self.expression = self.get_maths_obj(expression[0], "REMAINDER", expression[1])
        else:
            self.expression = self.get_maths_obj(self.raw_expression, "PLUS", 0)

    def calculate(self):
        if self.expression.get("operator") == "PLUS":
            return str(int(self.expression.get("value1")) + int(self.expression.get("value2")))
        elif self.expression.get("operator") == "MINUS":
            return str(int(self.expression.get("value1")) - int(self.expression.get("value2")))
        elif self.expression.get("operator") == "MULTIPLY":
            return str(int(self.expression.get("value1")) * int(self.expression.get("value2")))
        elif self.expression.get("operator") == "DIVIDE":
            return str(int(self.expression.get("value1")) / int(self.expression.get("value2")))
        elif self.expression.get("operator") == "POWER":
            return str(int(self.expression.get("value1")) ** int(self.expression.get("value2")))
        elif self.expression.get("operator") == "REMAINDER":
            return str(int(self.expression.get("value1")) % int(self.expression.get("value2")))