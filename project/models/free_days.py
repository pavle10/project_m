class FreeDays:

    def __init__(self, free_days_id, employee_id, start_date, end_date, total_days, reason):
        self.free_days_id = free_days_id
        self.employee_id = employee_id
        self.start_date = start_date
        self.end_date = end_date
        self.total_days = total_days
        self.reason = reason

    def get_free_days_id(self):
        return self.free_days_id

    def get_employee_id(self):
        return self.employee_id

    def get_start_daye(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date

    def get_total_days(self):
        return self.total_days

    def get_reason(self):
        return self.reason

    def __eq__(self, other):
        return isinstance(other, FreeDays) and self.free_days_id == other.free_days_id

    def __hash__(self):
        return hash(self.free_days_id)
