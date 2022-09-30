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

        in_string = False
        in_int = False
        string_type = ""
        current_value = ""

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
                if self.get_current_char() in "1234567890":
                    current_value = current_value + self.get_current_char()
                    in_int = True
                elif self.get_current_char() not in "1234567890" and in_int:
                    value.append(self.get_int_obj(current_value))
                    in_int = False
                    current_value = ""
                elif self.search_keyword("true"):
                    value.append(self.get_boolean_obj("true"))
                elif self.search_keyword("false"):
                    value.append(self.get_boolean_obj("false"))

                if self.get_current_char() == ")" and not in_string:
                    break

            if self.move_right():
                self.append_line()
            i += 1

        return value
    
    def parse(self):
        while self.current_line <= len(self.content):
            if self.search_keyword("printLn"):
                values = self.get_values()
                self.append_inline_func("printLn", values)

            if self.check_next_line_exists():
                self.move_right()
            else:
                break

        print(self.tree)