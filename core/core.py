from core.types import types


class core(types):
    def __init__(self, content):
        super().__init__()
        self.content = content.split("\n")
        self.current_line = 0
        self.char = 0
        self.recently_skiped_line = False

    def append_line(self):
        self.current_line += 1

    def move_right(self):
        if len(self.content[self.current_line]) == self.char and self.check_next_line_exists():
            self.append_line()
            self.char = 0
        else:
            if self.recently_skiped_line:
                self.recently_skiped_line = False
            else:
                self.char += 1

    def check_next_line_exists(self):
        if len(self.content)-1 == self.current_line and len(self.get_current_line()) == self.char:
            return False

        return True
    
    def skip_line(self):
        if self.check_next_line_exists():
            self.append_line()
        self.char = 0
        self.recently_skiped_line = True


    def get_current_line(self):
        return self.content[self.current_line]

    def get_current_char(self, previous=0):
        return self.content[self.current_line][self.char+previous]