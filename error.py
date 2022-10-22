############################
# ERROR
############################

class Error:
    def __init__(self, error_name, details):
        self.error_name = error_name
        self.details = details

    def as_string(self):
        result = f'{self.error_name}: {self.details}'
        return result

############################
# Illegal Charector Error
############################

class IllegalCharError(Error):
    def __init__(self, details):
        super().__init__('Illegal Charactor', details)