from core.core import core
from core.maths import Maths
from core.tree import functions


class parser(Maths, core):
    def __init__(self, content):
        core.__init__(self, content)
        Maths.__init__(self)

    def search_keyword(self, keyword):
        if self.content[self.current_line][self.char:self.char+len(keyword)] == keyword:
            self.char += len(keyword)

            return True
        
        return False

    def get_values(self):
        value = []
        args = []

        in_string = False
        in_int = False
        string_type = ""
        current_value = ""
        current_arg = ""
        
        self.move_right()

        while True:
            if self.get_current_char() == "\"" and not in_string:
                in_string = True
                string_type = "\""
            elif self.get_current_char() == "'" and not in_string:
                in_string = True
                string_type = "'"
            elif self.get_current_char() == string_type and in_string:
                in_string = False
                string_type = ""

                value.append(self.get_string_obj(current_value))

                current_value = ""
            elif in_string:
                current_value = current_value + self.get_current_char()
            elif not in_string:
                if self.get_current_char() in "1234567890+-*/^%":
                    current_value = current_value + self.get_current_char()
                    in_int = True
                elif self.get_current_char() not in "1234567890" and in_int:
                    self.set_expression(current_value)
                    self.parse_expression()
                    value.append(self.get_int_obj(self.calculate()))
                    in_int = False
                    current_value = ""
                    self.char -= 1
                elif self.search_keyword("true"):
                    value.append(self.get_boolean_obj("true"))
                elif self.search_keyword("false"):
                    value.append(self.get_boolean_obj("false"))
                elif self.get_current_char() == "," or self.get_current_char() == "(" or self.get_current_char() == ")" or self.get_current_char() == " " or self.get_current_line() == "":
                    pass
                else:
                    while True:
                        if self.get_current_char() != "," and self.get_current_char() != ")":
                            current_arg = current_arg + self.get_current_char()

                            self.move_right()
                        else:
                            args.append(current_arg)
                            current_arg = ""

                            break

                if self.get_current_char() == ")" and not in_string:
                    break

            self.move_right()

        in_string = False
        in_int = False
        string_type = ""
        current_value = ""
        current_arg = ""

        return value, args

    def parse_args(self, name, args):
        new_args = {}

        for i in range(len(args)):
            if "=" in args[i]:
                arg = args[i].split("=")
                if functions.get(name).get('allowed_args').get(arg[0]):
                    new_args[arg[0]] = self.get_arg_obj(arg[1])
                else:
                    print("Ay yo wtf man!")
            elif "=" not in args[i]:
                current_arg = functions.get(name).get('allowed_args').get(args[i])
                if current_arg:
                    if current_arg.get('isBoolean'):
                        new_args[args[i]] = self.get_arg_obj(current_arg.get('opposite'))
                else:
                    print("Ay yo wtf man!")
        
        for i in range(len(functions.get(name).get('allowed_args'))):
            allowed_args = list(functions.get(name).get('allowed_args').keys())

            if not new_args.get(allowed_args[i]):
                new_args[allowed_args[i]] = self.get_arg_obj(functions.get(name).get('allowed_args').get(allowed_args[i]).get('default'))

        return new_args

    def split_by_comma(self):
        start_pos = 0
        end_pos = 0

        while True:
            if self.search_keyword(" ") == " ":
                pass
            elif self.get_current_char() == "(":
                start_pos = self.char + 1
                self.move_right()
            elif self.get_current_char() == ")":
                end_pos = self.char
                break

            self.move_right()
        
        values = self.content[self.current_line][start_pos:end_pos].split(",")

        for i in range(len(values)):
            values[i] = values[i].replace(" ", "")

        return values
    
    def parse(self):
        while self.current_line != len(self.content):
            if self.get_current_line() == "":
                self.skip_line()
            elif self.search_keyword("#"):
                self.skip_line()
            elif self.search_keyword("printLn"):
                values, args = self.get_values()
                args = self.parse_args("printLn", args)
                self.append_inline_func("printLn", values, args)
            elif self.search_keyword("inputLn"):
                values, args = self.get_values()
                args = self.parse_args("inputLn", args)
                self.append_inline_func("inputLn", values, args)
            elif self.search_keyword("for"):
                value = self.split_by_comma()
                print(value)

            if self.check_next_line_exists():
                self.move_right()
            else:
                break

    def get_tree(self):
        return self.tree