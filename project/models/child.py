class Child:

    def __init__(self, child_id, first_name, last_name, identity_number, birthday, mother_id, father_id):
        self.first_name = first_name
        self.last_name = last_name
        self.child_id = child_id
        self.identity_number = identity_number
        self.birthday = birthday
        self.mother_id = mother_id
        self.mother_name = None
        self.father_id = father_id
        self.father_name = None

    @classmethod
    def from_values(cls, values):
        return cls(values[0], values[1], values[2], values[3], values[4], values[5], values[6])

    def get_child_id(self):
        return self.child_id

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, value):
        self.first_name = value

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, value):
        self.last_name = value

    def get_identity_number(self):
        return self.identity_number

    def set_identity_number(self, value):
        self.identity_number = value

    def get_birthday(self):
        return self.birthday

    def set_birthday(self, value):
        self.birthday = value

    def get_mother_id(self):
        return self.mother_id

    def set_mother_id(self, value):
        self.mother_id = value

    def get_mother_name(self):
        return self.mother_name

    def set_mother_name(self, value):
        self.mother_name = value

    def get_father_id(self):
        return self.father_id

    def set_father_id(self, value):
        self.father_id = value

    def get_father_name(self):
        return self.father_name

    def set_father_name(self, value):
        self.father_name = value

    def __eq__(self, other):
        return isinstance(other, Child) and self.child_id == other.child_id

    def __hash__(self):
        return hash(self.child_id)
