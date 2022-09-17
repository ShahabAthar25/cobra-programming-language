from core.tree import tree

class lexer(tree):
    def __init__(self, line, line_no):
        super().__init__()
        self.line = line
        self.line_no = line_no
        self.ch = 0

    def search_keywords(self, ch, keyword):
        keyword_lenght = len(keyword)

        if self.line[ch:ch+keyword_lenght] == keyword:
            self.ch = ch+keyword_lenght
            return True
        
        self.ch = ch+keyword_lenght
        return False

    def get_values(self):
        in_string = False
        i = 0

        while i < len(self.line):
            if self.line[i] == "\"":
                in_string = not in_string
            elif in_string:
                pass
            elif self.search_keywords(i, "terminal"):
                i = self.ch
                if self.search_keywords(i, ".out"):
                    self.tree_add_item("inline_func", "terminal.out", "Hello World", False)
                    i = self.ch
                elif self.search_keywords(i, ".in"):
                    input("terminal.in") 
                    i = self.ch
            else:
                self.throw_error("syntax", i)
                break
            i += 1