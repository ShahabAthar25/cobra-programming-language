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

    def get_string_obj(self, value):
        return {
            "type": "string",
            "value": value
        }

    def get_int_obj(self, value):
        return {
            "type": "int",
            "value": value
        }

    def get_boolean_obj(self, value):
        return {
            "type": "boolean",
            "value": value
        }