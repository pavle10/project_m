class Uniform:

    def __init__(self, uniform_id, name):
        self.uniform_id = uniform_id
        self.name = name

    def get_uniform_id(self):
        return self.uniform_id

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def __eq__(self, other):
        return isinstance(other, Uniform) and self.uniform_id == other.uniform_id

    def __hash__(self):
        return hash(self.uniform_id)
