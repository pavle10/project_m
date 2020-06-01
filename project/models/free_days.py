class FreeDays:

    def __init__(self, free_days_id, employee_id, start_date, end_date, total_days, reason):
        self.free_days_id = free_days_id
        self.employee_id = employee_id
        self.employee_name = ""
        self.start_date = start_date
        self.end_date = end_date
        self.total_days = total_days
        self.reason = reason

    @classmethod
    def from_values(cls, values):
        return cls(values[0], values[1], values[2], values[3], values[4], values[5])

    def get_free_days_id(self):
        return self.free_days_id

    def get_employee_id(self):
        return self.employee_id

    def get_employee_name(self):
        return self.employee_name

    def set_employee_name(self, value):
        self.employee_name = value

    def get_start_date(self):
        return self.start_date

    def set_start_date(self, value):
        self.start_date = value

    def get_end_date(self):
        return self.end_date

    def set_end_date(self, value):
        self.end_date = value

    def get_total_days(self):
        return self.total_days

    def set_total_days(self, value):
        self.total_days = value

    def get_reason(self):
        return self.reason

    def set_reason(self, value):
        self.reason = value

    def __eq__(self, other):
        return isinstance(other, FreeDays) and self.free_days_id == other.free_days_id

    def __hash__(self):
        return hash(self.free_days_id)

    def data_to_array(self):
        return [self.free_days_id, self.employee_id, self.start_date, self.end_date, self.total_days, self.reason]

    def update_data(self, values):
        self.start_date = values[2]
        self.end_date = values[3]
        self.total_days = values[4]
        self.reason = values[5]
