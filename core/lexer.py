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
        
        self.ch = ch+keyword_lenght
        return False

    def get_value(self, max_args, min_args):
        values = []

        current_string, in_string = "", False
        current_int = ""

        if self.line[self.ch] != "(":
            self.throw_error("syntax", self.ch)
        else:
            while True:
                if len(values) <= max_args:
                    if self.line[self.ch] == "\n":
                        self.new_line()
                        print("HEllo Wpr;d")
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
                        self.throw_error("syntax", self.ch)
                else:
                    self.throw_error("syntax", self.ch)
        
        return values

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
            elif self.search_keywords(i, "terminal"):
                i = self.ch
                if self.search_keywords(i, ".out"):
                    values = self.get_value(2, 1)
                    self.tree_add_item("inline_func", "terminal.out", values, False)
                    i = self.ch
                elif self.search_keywords(i, ".in"):
                    input("terminal.in") 
                    i = self.ch
                else:
                    self.throw_error("syntax", self.line_no)
            else:
                self.throw_error("syntax", i)
            i += 1