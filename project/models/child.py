class Child:

    def __init__(self, child_id, identity_number, birth_year, mother_id, father_id):
        self.child_id = child_id
        self.identity_number = identity_number
        self.birth_year = birth_year
        self.mother_id = mother_id
        self.father_id = father_id

    def get_child_id(self):
        return self.child_id

    def get_identity_number(self):
        return self.identity_number

    def get_birthday(self):
        return self.birth_year

    def get_mother_id(self):
        return self.mother_id

    def get_father_id(self):
        return self.father_id

    def __eq__(self, other):
        return isinstance(other, Child) and self.child_id == other.child_id

    def __hash__(self):
        return hash(self.child_id)
