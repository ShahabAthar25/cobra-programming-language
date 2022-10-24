############################
# ERROR
############################

class Error:
    def __init__(self, pos_start, pos_end, error_name, details):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details

    def as_string(self):
        text_split = self.pos_start.ftxt.split("\n")
        result = f'{self.error_name}: {self.details}'
        result += f'\nIn file {self.pos_start.fn} and line {self.pos_start.ln + 1}'
        result += f'\n\n|    {text_split[self.pos_start.ln]}'
        result += f'\n     '
        for i in range(self.pos_start.col):
            result += ' '
        result += "^"
        return result

############################
# ERRORS
############################

class IllegalCharError(Error):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, 'Illegal Charactor', details)

class InvalidSyntaxError(Error):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, 'Invalid Syntax', details)