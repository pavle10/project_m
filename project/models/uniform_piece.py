class UniformPiece:

    def __init__(self, uniform_piece_id, uniform_id, employee_id, size, quantity, additional, date):
        self.uniform_piece_id = uniform_piece_id
        self.uniform_id = uniform_id
        self.employee_id = employee_id
        self.size = size
        self.quantity = quantity
        self.additional = additional
        self.date = date

    def __eq__(self, other):
        return isinstance(other, UniformPiece) and self.uniform_piece_id == other.uniform_piece_id

    def __hash__(self):
        return hash(self.uniform_piece_id)
