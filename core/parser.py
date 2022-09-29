from core.core import core


class parser(core):
    def __init__(self, content):
        super().__init__(content)
    
    def parse(self):
        while self.current_line <= len(self.content):
            self.move_right()