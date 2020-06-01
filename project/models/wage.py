class Wage:

    def __init__(self, wage_id, employee_id, day, hour, meal):
        self.wage_id = wage_id
        self.employee_id = employee_id
        self.employee_name = ""
        self.day = day
        self.hour = hour
        self.meal = meal

    @classmethod
    def from_values(cls, values):
        return cls(values[0], values[1], values[2], values[3], values[4])

    def get_wage_id(self):
        return self.wage_id

    def get_employee_id(self):
        return self.employee_id

    def get_employee_name(self):
        return self.employee_name

    def set_employee_name(self, value):
        self.employee_name = value

    def get_day(self):
        return self.day

    def set_day(self, value):
        self.day = value

    def get_hour(self):
        return self.hour

    def set_hour(self, value):
        self.hour = value

    def get_meal(self):
        return self.meal

    def set_meal(self, value):
        self.meal = value

    def __eq__(self, other):
        return isinstance(other, Wage) and self.wage_id == other.wage_id

    def __hash__(self):
        return hash(self.wage_id)

    def data_to_array(self):
        return [self.wage_id, self.employee_id, self.day, self.hour, self.meal]

    def update_data(self, values):
        self.day = values[2]
        self.hour = values[3]
        self.meal = values[4]
