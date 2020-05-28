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

    @classmethod
    def from_values(cls, values):
        return cls(values[0], values[1], values[2], values[3], values[4],
                   values[5], values[6], values[7], values[8], values[9],
                   values[10], values[11], values[12], values[13], values[14], values[15])

    def get_employee_id(self):
        return self.employee_id

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, value):
        self.first_name = value

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, value):
        self.last_name = value

    def get_fathers_name(self):
        return self.fathers_name

    def set_fathers_name(self, value):
        self.fathers_name = value

    def get_identity_number(self):
        return self.identity_number

    def set_identity_number(self, value):
        self.identity_number = value

    def get_personal_card(self):
        return self.personal_card

    def set_personal_card(self, value):
        self.personal_card = value

    def get_qualification(self):
        return self.qualification

    def set_qualification(self, value):
        self.qualification = value

    def get_position(self):
        return self.position

    def set_position(self, value):
        self.position = value

    def get_saint_day(self):
        return self.saint_day

    def set_saint_day(self, value):
        self.saint_day = value

    def get_address(self):
        return self.address

    def set_address(self, value):
        self.address = value

    def get_account(self):
        return self.account

    def set_account(self, value):
        self.account = value

    def get_before_m(self):
        return self.before_m

    def set_before_m(self, value):
        self.before_m = value

    def get_start_date(self):
        return self.start_date

    def set_start_date(self, value):
        self.start_date = value

    def get_home_number(self):
        return self.home_number

    def set_home_number(self, value):
        self.home_number = value

    def get_mobile_number(self):
        return self.mobile_number

    def set_mobile_number(self, value):
        self.mobile_number = value

    def get_situation(self):
        return self.situation

    def set_situation(self, value):
        self.situation = value

    def __eq__(self, other):
        return isinstance(other, Employee) and self.employee_id == other.employee_id

    def __hash__(self):
        return hash(self.employee_id)

    def data_to_array(self):
        data_array = [self.employee_id, self.first_name, self.last_name, self.fathers_name, self.identity_number,
                      self.personal_card, self.qualification, self.position, self.saint_day, self.address, self.account,
                      self.before_m, self.start_date, self.home_number, self.mobile_number, self.situation]

        return data_array
