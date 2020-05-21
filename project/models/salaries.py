class Salary1:

    def __init__(self, salary_id, employee_id, net, gross, date):
        self.salary_id = salary_id
        self.employee_id = employee_id
        self.net = net
        self.gross = gross
        self.date = date

    def get_salary_id(self):
        return self.salary_id

    def get_employee_id(self):
        return self.employee_id

    def get_net(self):
        return self.net

    def get_gross(self):
        return self.gross

    def get_date(self):
        return self.date

    def __eq__(self, other):
        return isinstance(other, Salary1) and self.salary_id == other.salary_id

    def __hash__(self):
        return hash(self.salary_id)


class Salary2:
    def __init__(self, salary_id, employee_id, date, day, day_value,
                 hour, hour_value, meal, meal_value, payment, vacation, vacation_value, fix):
        self.salary_id = salary_id
        self.employee_id = employee_id
        self.date = date
        self.day = day
        self.day_value = day_value
        self.hour = hour
        self.hour_value = hour_value
        self.meal = meal
        self.meal_value = meal_value
        self.payment = payment
        self.vacation = vacation
        self.vacation_value = vacation_value
        self.fix = fix

    def get_salary_id(self):
        return self.salary_id

    def get_employee_id(self):
        return self.employee_id

    def get_date(self):
        return self.date

    def get_day(self):
        return self.day

    def get_day_value(self):
        return self.day_value

    def get_hour(self):
        return self.hour

    def get_hour_value(self):
        return self.hour_value

    def get_meal(self):
        return self.meal

    def get_meal_value(self):
        return self.meal_value

    def get_payment(self):
        return self.payment

    def get_vacation(self):
        return self.vacation

    def get_vacation_value(self):
        return self.vacation_value

    def get_fix(self):
        return self.fix

    def __eq__(self, other):
        return isinstance(other, Salary2) and self.salary_id == other.salary_id

    def __hash__(self):
        return hash(self.salary_id)

