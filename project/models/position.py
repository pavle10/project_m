class Position:

    def __init__(self, position_id, name, saturday):
        self.position_id = position_id
        self.name = name
        self.saturday = saturday

    def get_position_id(self):
        return self.position_id

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

    def set_saturday(self, value):
        self.saturday = value

    def change_saturday(self):
        self.saturday = not self.saturday

    def get_saturday(self):
        return self.saturday

    def __eq__(self, other):
        return isinstance(other, Position) and self.position_id == other.position_id

    def __hash__(self):
        return hash(self.position_id)
