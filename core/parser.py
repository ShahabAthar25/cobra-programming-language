from core.core import core


class parser(core):
    def __init__(self, content):
        super().__init__(content)

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
        in_arg = False
        string_type = ""
        current_value = ""
        current_arg = ""

        if self.get_current_char() != "(":
            print("ay yo")
            self.exit()
        
        self.move_right()

        i = 0
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
                if self.get_current_char() == "," or self.get_current_char() == "(" or self.get_current_char() == ")" or self.get_current_char() == " " or self.get_current_line() == "":
                    pass
                elif self.get_current_char() in "1234567890":
                    current_value = current_value + self.get_current_char()
                    in_int = True
                elif self.get_current_char() not in "1234567890" and in_int:
                    value.append(self.get_int_obj(current_value))
                    in_int = False
                    current_value = ""
                    self.char -= 1
                elif self.search_keyword("true"):
                    value.append(self.get_boolean_obj("true"))
                elif self.search_keyword("false"):
                    value.append(self.get_boolean_obj("false"))
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
            i += 1

        return value, args
    
    def parse(self):
        while self.current_line <= len(self.content):
            if self.search_keyword("#") or self.get_current_line() == "":
                self.skip_line()
            elif self.search_keyword("printLn"):
                values, args = self.get_values()
                self.append_inline_func("printLn", values, args)
            elif self.search_keyword("inputLn"):
                values, args = self.get_values()
                self.append_inline_func("inputLn", values, args)

            if self.check_next_line_exists():
                self.move_right()
            else:
                break

        print(self.tree)