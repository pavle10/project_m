class Uniform:

    def __init__(self, position_id, name):
        self.position_id = position_id
        self.name = name

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

    def __eq__(self, other):
        return isinstance(other, Uniform) and self.position_id == other.position_id

    def __hash__(self):
        return hash(self.position_id)
