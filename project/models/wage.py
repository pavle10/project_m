class Wage:

    def __init__(self, wage_id, employee_id, day, hour, meal):
        self.wage_id = wage_id
        self.employee_id = employee_id
        self.day = day
        self.hour = hour
        self.meal = meal

    def get_wage_id(self):
        return self.wage_id

    def get_employee_id(self):
        return self.employee_id

    def get_day(self):
        return self.day

    def get_hour(self):
        return self.hour

    def get_meal(self):
        return self.meal

    def __eq__(self, other):
        return isinstance(other, Wage) and self.wage_id == other.wage_id

    def __hash__(self):
        return hash(self.wage_id)