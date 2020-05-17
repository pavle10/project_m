class Employee:

    def __init__(self,
                 employee_id,
                 first_name,
                 last_name,
                 fathers_name,
                 identity_number,
                 personal_card,
                 qualification,
                 position,
                 saint_day,
                 address,
                 account,
                 before_m,
                 start_date,
                 home_number,
                 mobile_number,
                 situation):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.fathers_name = fathers_name
        self.identity_number = identity_number
        self.personal_card = personal_card
        self.qualification = qualification
        self.position = position
        self.saint_day = saint_day
        self.address = address
        self.account = account
        self.before_m = before_m
        self.start_date = start_date
        self.home_number = home_number
        self.mobile_number = mobile_number
        self.situation = situation

    def __eq__(self, other):
        return isinstance(other, Employee) and self.employee_id == other.employee_id

    def __hash__(self):
        return hash(self.employee_id)


