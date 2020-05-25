class UniformPiece:

    def __init__(self, uniform_piece_id, uniform_id, employee_id, size, quantity, additional, date):
        self.uniform_piece_id = uniform_piece_id
        self.uniform_id = uniform_id
        self.uniform_name = ""
        self.employee_id = employee_id
        self.size = size
        self.quantity = quantity
        self.additional = additional
        self.date = date

    def get_uniform_piece_id(self):
        return self.uniform_piece_id

    def get_uniform_id(self):
        return self.uniform_id

    def set_uniform_id(self, value):
        self.uniform_id = value

    def get_uniform_name(self):
        return self.uniform_name

    def set_uniform_name(self, value):
        self.uniform_name = value

    def get_employee_id(self):
        return self.employee_id

    def set_employee_id(self, value):
        self.employee_id = value

    def get_size(self):
        return self.size

    def set_size(self, value):
        self.size = value

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, value):
        self.quantity = value

    def get_additional(self):
        return self.additional

    def set_additional(self, value):
        self.additional = value

    def get_date(self):
        return self.date

    def set_date(self, value):
        self.date = value

    def __eq__(self, other):
        return isinstance(other, UniformPiece) and self.uniform_piece_id == other.uniform_piece_id

    def __hash__(self):
        return hash(self.uniform_piece_id)
