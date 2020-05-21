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
