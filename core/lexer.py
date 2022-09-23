from core.tree import tree

class lexer(tree):
    def __init__(self, line):
        super().__init__()
        self.line = line
        self.line_no = 0

    def new_line(self):
        self.line_no += 1

    def search_keywords(self, ch, keyword):
        keyword_lenght = len(keyword)

        if self.line[ch:ch+keyword_lenght] == keyword:
            self.ch = ch+keyword_lenght
            return True
        
        return False

    def get_value(self, min_args):
        values = []
        args = []

        current_string, in_string = "", False
        current_int = ""
        current_arg = ""

        if self.line[self.ch] != "(":
            self.throw_error("syntax", self.ch)
        else:
            while True:
                if self.line[self.ch] == "\n":
                    self.new_line()
                    self.ch += 1
                elif self.line[self.ch] == "(" and not in_string or self.line[self.ch] == " " and not in_string or self.line[self.ch] == "," and not in_string:
                    self.ch += 1
                elif self.line[self.ch] == "\"" or self.line[self.ch] == "'":
                    in_string = not in_string
                    if not in_string:
                        values.append({
                            'value': current_string,
                            'type': 'string'
                        })
                        current_string = ""
                    self.ch += 1
                elif in_string:
                    current_string = current_string + self.line[self.ch]
                    self.ch += 1
                elif self.line[self.ch] in "1234567890" and self.line[self.ch+1] in "1234567890":
                    current_int = current_int + self.line[self.ch]
                    self.ch += 1
                elif self.line[self.ch] in "1234567890" and not self.line[self.ch+1] in "1234567890":
                    current_int = current_int + self.line[self.ch]
                    values.append({
                            'value': current_int,
                            'type': 'int'
                        })
                    current_int = ""
                    self.ch += 1
                elif self.line[self.ch:self.ch+4] == "true":
                    values.append({
                            'value': "true",
                            'type': 'boolean'
                        })
                    self.ch += 4
                elif self.line[self.ch:self.ch+5] == "false":
                    values.append({
                            'value': "false",
                            'type': 'boolean'
                        })
                    self.ch += 5
                elif self.line[self.ch] == ")":
                    self.ch += 1
                    if len(values) < min_args:
                        self.throw_error("syntax", self.ch)
                    break
                else:
                    while not self.line[self.ch] == "," and not self.line[self.ch] == " " and not self.line[self.ch] == ")":
                        current_arg = current_arg + self.line[self.ch]
                        self.ch += 1
                    args.append(current_arg)
                    current_arg = ""
        
        return values, args

    def parse_var(self):
        self.ch += 1

        name = ""
        _type = ""
        value = ""

        in_value = False
        in_string = False
        string_type = ""

        while self.line[self.ch] != "\n":
            if self.line[self.ch] == "\"" and not in_string and in_value:
                in_string = True
                string_type = "\""
            elif self.line[self.ch] == "'" and not in_string and in_value:
                in_string = True
                string_type = "'"
            elif self.line[self.ch] == string_type and in_string and in_value:
                in_string = False
            elif self.search_keywords(self.ch, "::") and not in_value:
                if self.search_keywords(self.ch, "String"):
                    _type = "String"
                elif self.search_keywords(self.ch, "Integer"):
                    _type = "Integer"
                elif self.search_keywords(self.ch, "Boolean"):
                    _type = "Boolean"
                elif self.search_keywords(self.ch, "Float"):
                    _type = "Float"
                elif self.search_keywords(self.ch, "Array"):
                    _type = "Array"
                elif self.search_keywords(self.ch, "Object"):
                    _type = "Object"
                else:
                    self.throw_error("syntax", self.ch)
            elif self.line[self.ch] == "=" or in_value:
                in_value = True
                if not in_string and self.line[self.ch] == " " or not in_string and self.line[self.ch] == "=":
                    pass
                else:
                    value =  value + self.line[self.ch]
            else:
                name = name + self.line[self.ch]

            self.ch +=1
        
        return name, _type, value

    def commit(self):
        in_string = False
        i = 0

        while i < len(self.line):
            if self.line[i] == "\n":
                self.new_line()
            elif self.line[i] == "\"":
                in_string = not in_string
            elif in_string:
                pass
            elif self.line[i] == "#":
                i += 1
                while self.line[i] != "\n":
                    i += 1
                    if len(self.line) == i:
                        break
            elif self.search_keywords(i, "printLn"):
                i = self.ch
                values, args = self.get_value(1)
                self.tree_add_inline_func("printLn", values, args)
                i = self.ch
            elif self.search_keywords(i, "inputLn"):
                i = self.ch
                values, args = self.get_value(1)
                self.tree_add_inline_func("inputLn", values, args)
                i = self.ch
            elif self.search_keywords(i, "var"):
                name, _type, value = self.parse_var()
                self.tree_add_variable(name, _type, value)
                i = self.ch
            else:
                self.throw_error("syntax", i)
            i += 1