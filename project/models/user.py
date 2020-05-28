from project.utils.funcs import convert_level


class User:

    def __init__(self, username, level):
        self._username = username
        self._level = convert_level(level)

    @classmethod
    def from_values(cls, values):
        return cls(values[0], values[1])

    def get_username(self):
        return self._username

    def get_level(self):
        return self._level
