class types:
    def __init__(self):
        self.tree = []

    def append_inline_func(self, name, value=[], extras=[]):
        self.tree.append({
            "type": "inline_func",
            "name": name,
            "value": value,
            "args": extras,
        })