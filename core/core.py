from core.types import types


class core(types):
    def __init__(self, content):
        super().__init__()
        self.content = content.split("\n")
        self.current_line = 0
        self.char = 0

    def append_line(self):
        if len(self.content)-1 <= self.current_line:
            exit()
        else:
            self.current_line += 1

    def move_right(self):
        if len(self.content[self.current_line]) == self.char:
            self.append_line()
            self.char = 0
        else:
            self.char += 1

    def get_current_line(self):
        return self.content[self.current_line]

    def get_current_char(self):
        return self.content[self.current_line][self.char]