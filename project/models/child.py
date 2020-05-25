class Child:

    def __init__(self, child_id, identity_number, birth_year, mother_id, father_id):
        self.child_id = child_id
        self.identity_number = identity_number
        self.birth_year = birth_year
        self.mother_id = mother_id
        self.mother_name = None
        self.father_id = father_id
        self.father_name = None

    def get_child_id(self):
        return self.child_id

    def get_identity_number(self):
        return self.identity_number

    def set_identity_number(self, value):
        self.identity_number = value

    def get_birth_year(self):
        return self.birth_year

    def set_birth_year(self, value):
        self.birth_year = value

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
