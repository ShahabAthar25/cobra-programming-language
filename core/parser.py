from core.core import core


class parser(core):
    def __init__(self, content):
        super().__init__(content)

    def search_keyword(self, keyword):
        if self.content[self.current_line][self.char:self.char+len(keyword)] == keyword:
            self.char = self.char + len(keyword)

            return True
        
        return False

    def get_values(self):
        value = []

        in_string = ""
        string_type = ""
        current_value = ""

        i = 0
        while i != len(self.get_current_line()):
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
            elif self.get_current_char() == ")":
                break

            self.move_right()
            i += 1

        return value
    
    def parse(self):
        while self.current_line <= len(self.content):
            if self.search_keyword("printLn"):
                print(self.get_values())
            self.move_right()