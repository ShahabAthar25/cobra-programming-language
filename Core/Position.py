class Position:
    def __init__(self, pos, ln, col):
        self.pos = pos
        self.ln = ln
        self.col = col

    def advance(self, current_char):
        self.pos += 1
        self.col += 1

        if current_char == "\n":
            self.ln += 1
            self.col = 0

        return self

    def copy(self):
        return Position(self.pos, self.ln, self.col)