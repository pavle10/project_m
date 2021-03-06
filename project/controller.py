import sys
from PyQt5.QtWidgets import QApplication

from project.managers.database_manager import DatabaseManager
from project.managers.view_manager import ViewManager
from project.utils.enums import Actions, ResponseStatus
from project.models.user import User
from project.models.response import Response
from project.utils import funcs, strings as strs


class Controller:

    def __init__(self):
        self._app = QApplication(sys.argv)

        self._database_manager = DatabaseManager()

        self._init_models()

        self._view_manager = ViewManager(self)

    def _init_models(self):
        self._user = None

        response = self._database_manager.actions(Actions.all_employees)
        if response.get_status() == ResponseStatus.success:
            self._employees = response.get_data()

        response = self._database_manager.actions(Actions.all_positions)
        if response.get_status() == ResponseStatus.success:
            self._positions = response.get_data()

        response = self._database_manager.actions(Actions.all_uniforms)
        if response.get_status() == ResponseStatus.success:
            self._uniforms = response.get_data()

        response = self._database_manager.actions(Actions.all_uniform_pieces)
        if response.get_status() == ResponseStatus.success:
            self._uniform_pieces = response.get_data()

        response = self._database_manager.actions(Actions.all_children)
        if response.get_status() == ResponseStatus.success:
            self._children = response.get_data()

        response = self._database_manager.actions(Actions.all_free_days)
        if response.get_status() == ResponseStatus.success:
            self._all_free_days = response.get_data()

        response = self._database_manager.actions(Actions.all_wages)
        if response.get_status() == ResponseStatus.success:
            self._wages = response.get_data()

        self._update_uniform_pieces_name()
        self._update_children_parents()
        self._update_uniform_pieces_employees_names()
        self._update_free_days_employees_names()
        self._update_wages_employees_names()

    def run(self):
        self._view_manager.actions(Actions.show)

        return self._app.exec_()

    def set_user(self, user):
        self._user = user

    def get_username(self):
        return self._user.get_username()

    def get_user_privilege(self):
        return self._user.get_level()

    def actions(self, action, values=None):
        if action == Actions.login:
            return self._login(values)
        elif action == Actions.add_position:
            return self._add_position(values)
        elif action == Actions.add_employee:
            return self._add_employee(values)
        elif action == Actions.add_uniform:
            return self._add_uniform(values)
        elif action == Actions.add_uniform_piece:
            return self._add_uniform_piece(values)
        elif action == Actions.add_child:
            return self._add_child(values)
        elif action == Actions.add_free_days:
            return self._add_free_days(values)
        elif action == Actions.add_wage:
            return self._add_wage(values)
        elif action == Actions.add_salary_1:
            return self._add_salary_1(values)
        elif action == Actions.add_salary_2:
            return self._add_salary_2(values)
        elif action == Actions.all_positions:
            return self._get_all_positions()
        elif action == Actions.all_employees:
            return self._get_all_employees()
        elif action == Actions.all_children:
            return self._get_all_children()
        elif action == Actions.all_uniforms:
            return self._get_all_uniforms()
        elif action == Actions.employee_uniform_pieces:
            return self._get_employee_uniform_pieces(values)
        elif action == Actions.employee_free_days:
            return self._get_employee_free_days(values)
        elif action == Actions.employee_wage:
            return self._get_employee_wage(values)
        elif action == Actions.employee_salaries_1:
            return self._get_employee_salaries_1(values)
        elif action == Actions.employee_salaries_2:
            return self._get_employee_salaries_2(values)
        elif action == Actions.update_employee:
            return self._update_employee(values)
        elif action == Actions.update_position:
            return self._update_position(values)
        elif action == Actions.update_child:
            return self._update_child(values)
        elif action == Actions.update_uniform:
            return self._update_uniform(values)
        elif action == Actions.update_uniform_piece:
            return self._update_uniform_piece(values)
        elif action == Actions.update_free_days:
            return self._update_free_days(values)
        elif action == Actions.update_wage:
            return self._update_wage(values)
        elif action == Actions.update_salary_1:
            return self._update_salary_1(values)
        elif action == Actions.update_salary_2:
            return self._update_salary_2(values)
        elif action == Actions.delete_employee:
            return self._delete_employee(values)
        elif action == Actions.delete_position:
            return self._delete_position(values)
        elif action == Actions.delete_child:
            return self._delete_child(values)
        elif action == Actions.delete_uniform:
            return self._delete_uniform(values)
        elif action == Actions.delete_uniform_piece:
            return self._delete_uniform_piece(values)
        elif action == Actions.delete_free_days:
            return self._delete_free_days(values)
        elif action == Actions.delete_wage:
            return self._delete_wage(values)
        elif action == Actions.delete_salary_1:
            return self._delete_salary_1(values)
        elif action == Actions.delete_salary_2:
            return self._delete_salary_2(values)

    def _update_uniform_pieces_name(self, indices=None):
        indices = range(len(self._uniform_pieces)) if indices is None else indices

        for index in indices:
            piece = self._uniform_pieces[index]

            for uniform in self._uniforms:
                if uniform.get_uniform_id() == piece.get_uniform_id():
                    piece.set_uniform_name(uniform.get_name())
                    break

    def _update_children_parents(self, indices=None):
        indices = range(len(self._children)) if indices is None else indices

        for index in indices:
            child = self._children[index]
            mother_id = child.get_mother_id()
            father_id = child.get_father_id()

            for employee in self._employees:
                if employee.get_employee_id() == mother_id:
                    child.set_mother_name(funcs.employee_unique_name(employee))
                elif employee.get_employee_id() == father_id:
                    child.set_father_name(funcs.employee_unique_name(employee))

    def _update_uniform_pieces_employees_names(self, indices=None):
        indices = range(len(self._uniform_pieces)) if indices is None else indices

        for index in indices:
            uni_piece = self._uniform_pieces[index]
            uni_piece.set_employee_name(self._get_employee_unique_name(uni_piece.get_employee_id()))

    def _update_free_days_employees_names(self, indices=None):
        indices = range(len(self._all_free_days)) if indices is None else indices

        for index in indices:
            free_days = self._all_free_days[index]
            free_days.set_employee_name(self._get_employee_unique_name(free_days.get_employee_id()))

    def _update_wages_employees_names(self, indices=None):
        indices = range(len(self._wages)) if indices is None else indices

        for index in indices:
            wage = self._wages[index]
            wage.set_employee_name(self._get_employee_unique_name(wage.get_employee_id()))

    def _login(self, values):
        # Input data validation
        if not funcs.check_required_fields(values[0], values[1]):
            return Response(ResponseStatus.fail, strs.MISSING_CREDENTIALS_MSG)

        # Check credentials
        response = self._database_manager.actions(Actions.login, values)

        if response.get_status() == ResponseStatus.success:
            self._user = User.from_values(response.get_data()[0])
            response.set_message(strs.SUCCESSFUL_LOGIN_MSG.format(username=self._user.get_username()))

        return response

    def _add_position(self, values):
        # Input data validation
        # Check required fields
        if not funcs.check_required_fields(values[0]):
            return Response(ResponseStatus.fail, strs.REQUIRED_FIELDS_NOT_FILLED_MSG)

        values[1] = funcs.convert_saturday(values[1])

        response = self._database_manager.actions(Actions.add_position, values)

        if response.get_status() == ResponseStatus.success:
            self._positions.append(response.get_data())

        return response

    def _add_employee(self, values):
        # Input data validation
        # Check required fields
        if not funcs.check_required_fields(values[0], values[1], values[3], values[6], values[8]):
            return Response(ResponseStatus.fail, strs.REQUIRED_FIELDS_NOT_FILLED_MSG)

        # Check before m fields
        before_m = values[10]

        if not funcs.convert_to_int(before_m, range(3)):
            return Response(ResponseStatus.fail, strs.NOT_INTEGER_MSG)

        years = before_m[0]
        months = before_m[1]
        days = before_m[2]

        if years < 0 or months < 0 or months > 11 or days < 0 or days > 30:
            # TODO write to log
            return Response(ResponseStatus.fail, strs.INVALID_DATE_FORMAT_MSG)

        values[10] = funcs.to_days(years, months, days)

        position_id = self._get_position_id(values[6])

        # Check position id
        if position_id is None:
            # TODO write to log
            return Response(ResponseStatus.fail, strs.INTERNAL_ERROR_MSG)

        values[6] = position_id
        response = self._database_manager.actions(Actions.add_employee, values)

        if response.get_status() == ResponseStatus.success:
            self._employees.append(response.get_data())

        return response

    def _add_uniform(self, values):
        # Input data validation
        # Check required fields
        if not funcs.check_required_fields(values[0]):
            return Response(ResponseStatus.fail, strs.REQUIRED_FIELDS_NOT_FILLED_MSG)

        response = self._database_manager.actions(Actions.add_uniform, values)

        if response.get_status() == ResponseStatus.success:
            self._uniforms.append(response.get_data())

        return response

    def _add_uniform_piece(self, values):
        # Input data validation
        # Check required fields
        if not funcs.check_required_fields(values[0], values[1], values[2], values[3]):
            return Response(ResponseStatus.fail, strs.REQUIRED_FIELDS_NOT_FILLED_MSG)

        if not funcs.convert_to_int(values, [2, 3]):
            return Response(ResponseStatus.fail, strs.NOT_INTEGER_MSG)

        if values[2] < 0 or values[3] < 0:
            # TODO write to log
            return Response(ResponseStatus.fail, strs.INVALID_MEASURE_MSG)

        uniform_id = self._get_uniform_id(values[0])
        employee_id = self._get_employee_id(values[1])

        if uniform_id is None or employee_id is None:
            # TODO write to log
            return Response(ResponseStatus.fail, strs.INTERNAL_ERROR_MSG)

        values[0] = uniform_id
        values[1] = employee_id

        response = self._database_manager.actions(Actions.add_uniform_piece, values)

        if response.get_status() == ResponseStatus.success:
            self._uniform_pieces.append(response.get_data())
            self._update_uniform_pieces_name([-1])
            self._update_uniform_pieces_employees_names([-1])

        return response

    def _add_child(self, values):
        # Input data validation
        # Check required fields
        if not funcs.check_required_fields(values[0], values[1], values[3]):
            return Response(ResponseStatus.fail, strs.REQUIRED_FIELDS_NOT_FILLED_MSG)

        mother_id = self._get_employee_id(values[4])
        father_id = self._get_employee_id(values[5])

        if mother_id is None and father_id is None:
            return Response(ResponseStatus.fail, strs.CHILD_ONE_PARENT_REQUIRED_MSG)

        values[4] = mother_id
        values[5] = father_id

        response = self._database_manager.actions(Actions.add_child, values)

        if response.get_status() == ResponseStatus.success:
            self._children.append(response.get_data())
            self._update_children_parents([-1])

        return response

    def _add_free_days(self, values):
        # Input data validation
        # Check required fields
        if not funcs.check_required_fields(values[0], values[4]):
            return Response(ResponseStatus.fail, strs.REQUIRED_FIELDS_NOT_FILLED_MSG)

        if values[3] <= 0:
            return Response(ResponseStatus.fail, strs.INVALID_DATES_MSG)

        employee_id = self._get_employee_id(values[0])

        if employee_id is None:
            return Response(ResponseStatus.fail, strs.INTERNAL_ERROR_MSG)

        values[0] = employee_id

        response = self._database_manager.actions(Actions.add_free_days, values)

        if response.get_status() == ResponseStatus.success:
            self._all_free_days.append(response.get_data())
            self._update_free_days_employees_names([-1])

        return response

    def _add_wage(self, values):
        # Input data validation
        # Check required fields
        if not funcs.check_required_fields(values[0], values[1], values[2], values[3]):
            return Response(ResponseStatus.fail, strs.REQUIRED_FIELDS_NOT_FILLED_MSG)

        if not funcs.convert_to_int(values, [1, 2, 3]):
            return Response(ResponseStatus.fail, strs.NOT_INTEGER_MSG)

        if values[1] < 0 or values[2] < 0 or values[3] < 0:
            # TODO write to log
            return Response(ResponseStatus.fail, strs.INVALID_MEASURE_MSG)

        employee_id = self._get_employee_id(values[0])

        if employee_id is None:
            return Response(ResponseStatus.fail, strs.INTERNAL_ERROR_MSG)

        values[0] = employee_id

        response = self._database_manager.actions(Actions.add_wage, values)

        if response.get_status() == ResponseStatus.success:
            self._wages.append(response.get_data())
            self._update_wages_employees_names([-1])

        return response

    def _add_salary_1(self, values):
        # Input data validation
        # Check required fields
        if not funcs.check_required_fields(values[0], values[1], values[2]):
            return Response(ResponseStatus.fail, strs.REQUIRED_FIELDS_NOT_FILLED_MSG)

        if not funcs.convert_to_int(values, [1, 2]):
            return Response(ResponseStatus.fail, strs.NOT_INTEGER_MSG)

        if values[1] < 0 or values[2] < 0:
            # TODO write to log
            return Response(ResponseStatus.fail, strs.INVALID_MEASURE_MSG)

        if values[1] > values[2]:
            return Response(ResponseStatus.fail, strs.INVALID_NET_GROSS_RATIO_MSG)

        employee_id = self._get_employee_id(values[0])

        if employee_id is None:
            return Response(ResponseStatus.fail, strs.INTERNAL_ERROR_MSG)

        values[0] = employee_id

        return self._database_manager.actions(Actions.add_salary_1, values)

    def _add_salary_2(self, values):
        # Input data validation
        if not funcs.convert_to_int(values, [2, 4, 6, 8, 9, 10, 11]):
            return Response(ResponseStatus.fail, strs.NOT_INTEGER_MSG)

        if values[2] < 0 or values[4] < 0 or values[6] < 0 or values[8] < 0 \
                or values[9] < 0 or values[10] < 0 or values[11] < 0:
            # TODO write to log
            return Response(ResponseStatus.fail, strs.INVALID_MEASURE_MSG)

        if values[11] > 0 and (values[2] > 0 or values[4] > 0 or values[6] > 0 or
                               values[8] > 0 or values[9] > 0 or values[10] > 0):
            return Response(ResponseStatus.fail, strs.NOT_ALLOWED_FIX_AND_OTHER_MSG)

        employee_id = self._get_employee_id(values[0])

        if employee_id is None:
            return Response(ResponseStatus.fail, strs.INTERNAL_ERROR_MSG)

        response = self._get_employee_wage(values)
        wage = response.get_data()
        if response.get_status() == ResponseStatus.fail or wage is None:
            return Response(ResponseStatus.fail, strs.WAGE_FOR_EMPLOYEE_MISSING_MSG.format(employee=values[0]))

        values[0] = employee_id
        values[3] = wage[0].get_day()
        values[5] = wage[0].get_hour()
        values[7] = wage[0].get_meal()

        return self._database_manager.actions(Actions.add_salary_2, values)

    def _get_all_positions(self):
        return self._positions

    def _get_position_id(self, name):
        for position in self._positions:
            if position.get_name() == name:
                return position.get_position_id()

        return None

    def _get_all_employees(self):
        return self._employees

    def _get_employee_unique_name(self, employee_id):
        for employee in self._employees:
            if employee.get_employee_id() == employee_id:
                return f"{employee.get_first_name()} {employee.get_last_name()} {employee.get_identity_number()}"

        return None

    def _get_employee_id(self, value):
        if value is None:
            return None

        values = value.split(' ')

        if len(values) != 3:
            return None

        first_name = values[0]
        last_name = values[1]
        identity_number = values[2]

        for employee in self._employees:
            if employee.get_first_name() == first_name and\
                    employee.get_last_name() == last_name and\
                    employee.get_identity_number() == identity_number:
                return employee.get_employee_id()

        return None

    def _get_all_children(self):
        return self._children

    def _get_child_id(self, values):
        for child in self._children:
            if (child.get_identity_number() == values[0] and child.get_birth_year() == values[1]
               and child.get_mother_name() == values[2] and child.get_father_name() == values[3]):
                return child.get_child_id()

        return None

    def _get_all_uniforms(self):
        return self._uniforms

    def _get_uniform_id(self, name):
        for uniform in self._uniforms:
            if uniform.get_name() == name:
                return uniform.get_uniform_id()

        return None

    def _get_uniform_name(self, uniform_id):
        for uniform in self._uniforms:
            if uniform.get_uniform_id() == uniform_id:
                return uniform.get_name()

        return ""

    def _get_employee_uniform_pieces(self, values):
        start_date = values[1]
        end_date = values[2]

        if start_date > end_date:
            return Response(ResponseStatus.fail, strs.INVALID_DATES_MSG)

        result = list()

        if values[0] == strs.ALL:
            for piece in self._uniform_pieces:
                if start_date <= piece.get_date() <= end_date:
                    result.append(piece)
        else:
            employee_id = self._get_employee_id(values[0])

            if employee_id is None:
                return Response(ResponseStatus.fail, strs.INTERNAL_ERROR_MSG)

            for piece in self._uniform_pieces:
                if piece.get_employee_id() == employee_id and start_date <= piece.get_date() <= end_date:
                    result.append(piece)

        return Response(ResponseStatus.success, strs.UNIFORM_PIECE_EMP_SUCC_MSG, result)

    def _get_employee_free_days(self, values):
        result = list()
        start_date = values[1]
        end_date = values[2]

        if start_date > end_date:
            return Response(ResponseStatus.fail, strs.INVALID_DATES_MSG)

        if values[0] == strs.ALL:
            for free_days in self._all_free_days:
                if start_date <= free_days.get_start_date() and free_days.get_end_date() <= end_date:
                    result.append(free_days)

        else:
            employee_id = self._get_employee_id(values[0])

            if employee_id is None:
                return Response(ResponseStatus.fail, strs.INTERNAL_ERROR_MSG)

            for free_days in self._all_free_days:
                if free_days.get_employee_id() == employee_id \
                        and start_date <= free_days.get_start_date() \
                        and free_days.get_end_date() <= end_date:
                    result.append(free_days)

        return Response(ResponseStatus.success, strs.FREE_DAYS_EMP_SUCC_MSG, result)

    def _get_employee_wage(self, values):
        if values[0] == strs.ALL:
            return Response(ResponseStatus.success, strs.WAGE_EMP_SUCC_MSG, self._wages)

        employee_id = self._get_employee_id(values[0])

        for wage in self._wages:
            if wage.get_employee_id() == employee_id:
                return Response(ResponseStatus.success, strs.WAGE_EMP_SUCC_MSG, [wage])

        return Response(ResponseStatus.fail, strs.WAGE_EMP_FAIL_MSG)

    def _get_employee_salaries_1(self, values):
        start_date = values[1]
        end_date = values[2]

        if start_date > end_date:
            return Response(ResponseStatus.fail, strs.INVALID_DATES_MSG)

        if values[0] == strs.ALL:
            response = self._database_manager.actions(Actions.salaries_1_between_dates, [start_date, end_date])
        else:
            employee_id = self._get_employee_id(values[0])

            if employee_id is None:
                return Response(ResponseStatus.fail, strs.INTERNAL_ERROR_MSG)

            values[0] = employee_id

            response = self._database_manager.actions(Actions.employee_salaries_1, values)

        if response.get_status() == ResponseStatus.success:
            result = list()

            for data in response.get_data():
                employee_name = self._get_employee_unique_name(data[1])
                result.append(funcs.transform_salary_data(employee_name, data))

            response.set_data(result)

        return response

    def _get_employee_salaries_2(self, values):
        start_date = values[1]
        end_date = values[2]

        if start_date > end_date:
            return Response(ResponseStatus.fail, strs.INVALID_DATES_MSG)

        if values[0] == strs.ALL:
            response = self._database_manager.actions(Actions.salaries_2_between_dates, [start_date, end_date])
        else:
            employee_id = self._get_employee_id(values[0])

            if employee_id is None:
                return Response(ResponseStatus.fail, strs.INTERNAL_ERROR_MSG)

            values[0] = employee_id

            response = self._database_manager.actions(Actions.employee_salaries_2, values)

        if response.get_status() == ResponseStatus.success:
            result = list()

            for data in response.get_data():
                employee_name = self._get_employee_unique_name(data[1])
                result.append(funcs.transform_salary_data(employee_name, data))

            response.set_data(result)

        return response

    def _update_employee(self, values):
        # Input data validation
        # Check required fields
        if not funcs.check_required_fields(values[1], values[2], values[4], values[7], values[9]):
            return Response(ResponseStatus.fail, strs.REQUIRED_FIELDS_NOT_FILLED_MSG)

        # Check before m fields
        before_m = values[11]

        if not funcs.convert_to_int(before_m, range(3)):
            return Response(ResponseStatus.fail, strs.NOT_INTEGER_MSG)

        years = before_m[0]
        months = before_m[1]
        days = before_m[2]

        if years < 0 or months < 0 or months > 11 or days < 0 or days > 30:
            # TODO write to log
            return Response(ResponseStatus.fail, strs.INVALID_DATE_FORMAT_MSG)

        values[11] = funcs.to_days(years, months, days)

        position_id = self._get_position_id(values[7])

        # Check position id
        if position_id is None:
            # TODO write to log
            return Response(ResponseStatus.fail, strs.INTERNAL_ERROR_MSG)

        values[7] = position_id

        response = self._database_manager.actions(Actions.update_employee, values)

        if response.get_status() == ResponseStatus.success:
            for employee in self._employees:
                if employee.get_employee_id() == values[0]:
                    employee.update_data(values)
                    break

        return response

    def _update_position(self, values):
        # Input data validation
        # Check required fields
        if not funcs.check_required_fields(values[1], values[2]):
            return Response(ResponseStatus.fail, strs.REQUIRED_FIELDS_NOT_FILLED_MSG)

        position_id = self._get_position_id(values[0])

        if position_id is None:
            return Response(ResponseStatus.fail, strs.INTERNAL_ERROR_MSG)

        values[0] = position_id
        response = self._database_manager.actions(Actions.update_position, values)

        if response.get_status() == ResponseStatus.success:
            for position in self._positions:
                if position.get_position_id() == values[0]:
                    position.update_data(values)
                    break

        return response

    def _update_child(self, values):
        # Input data validation
        # Check required fields
        if not funcs.check_required_fields(values[1], values[2], values[4]):
            return Response(ResponseStatus.fail, strs.REQUIRED_FIELDS_NOT_FILLED_MSG)

        if values[6] == "" and values[8] == "":
            return Response(ResponseStatus.fail, strs.CHILD_ONE_PARENT_REQUIRED_MSG)

        mother_id = self._get_employee_id(values[6])
        father_id = self._get_employee_id(values[8])

        if mother_id is None and father_id is None:
            return Response(ResponseStatus.fail, strs.INTERNAL_ERROR_MSG)

        query_values = [values[0], values[1], values[2], values[3], values[4], mother_id, father_id]
        values[5] = mother_id
        values[7] = father_id

        response = self._database_manager.actions(Actions.update_child, query_values)

        if response.get_status() == ResponseStatus.success:
            for child in self._children:
                if child.get_child_id() == values[0]:
                    child.update_data(values)
                    break

        return response

    def _update_uniform(self, values):
        # Input data validation
        # Check required fields
        if not funcs.check_required_fields(values[1]):
            return Response(ResponseStatus.fail, strs.REQUIRED_FIELDS_NOT_FILLED_MSG)

        uniform_id = self._get_uniform_id(values[0])

        if uniform_id is None:
            # TODO write to log
            return Response(ResponseStatus.fail, strs.INTERNAL_ERROR_MSG)

        values[0] = uniform_id
        response = self._database_manager.actions(Actions.update_uniform, values)

        if response.get_status() == ResponseStatus.success:
            for uniform in self._uniforms:
                if uniform.get_uniform_id() == uniform_id:
                    uniform.set_name(values[1])
                    break

        return response

    def _update_uniform_piece(self, values):
        # Input data validation
        # Check required fields
        if not funcs.check_required_fields(values[1], values[3], values[4], values[6]):
            return Response(ResponseStatus.fail, strs.REQUIRED_FIELDS_NOT_FILLED_MSG)

        if not funcs.convert_to_int(values, [3, 4]):
            return Response(ResponseStatus.fail, strs.NOT_INTEGER_MSG)

        if values[3] < 0 or values[4] < 0:
            return Response(ResponseStatus.fail, strs.INVALID_MEASURE_MSG)

        uniform_name = self._get_uniform_name(values[1])

        if uniform_name is None:
            # TODO write to log
            return Response(ResponseStatus.fail, strs.INTERNAL_ERROR_MSG)

        response = self._database_manager.actions(Actions.update_uniform_piece, values)

        if response.get_status() == ResponseStatus.success:
            for uniform_piece in self._uniform_pieces:
                if uniform_piece.get_uniform_piece_id() == values[0]:
                    uniform_piece.update_data(values)
                    uniform_piece.set_uniform_name(uniform_name)
                    break

        return response

    def _update_free_days(self, values):
        # Input data validation
        # Check required fields
        if not funcs.check_required_fields(values[5]):
            return Response(ResponseStatus.fail, strs.REQUIRED_FIELDS_NOT_FILLED_MSG)

        if values[4] <= 0:
            return Response(ResponseStatus.fail, strs.INVALID_DATES_MSG)

        response = self._database_manager.actions(Actions.update_free_days, values)

        if response.get_status() == ResponseStatus.success:
            for free_days in self._all_free_days:
                if free_days.get_free_days_id() == values[0]:
                    free_days.update_data(values)
                    break

        return response

    def _update_wage(self, values):
        # Input data validation
        # Check required fields
        if not funcs.check_required_fields(values[2], values[3], values[4]):
            return Response(ResponseStatus.fail, strs.REQUIRED_FIELDS_NOT_FILLED_MSG)

        if not funcs.convert_to_int(values, [2, 3, 4]):
            return Response(ResponseStatus.fail, strs.NOT_INTEGER_MSG)

        if values[2] < 0 or values[3] < 0 or values[4] < 0:
            # TODO write to log
            return Response(ResponseStatus.fail, strs.INVALID_MEASURE_MSG)

        response = self._database_manager.actions(Actions.update_wage, values)

        if response.get_status() == ResponseStatus.success:
            for wage in self._wages:
                if wage.get_wage_id() == values[0]:
                    wage.update_data(values)
                    break

        return response

    def _update_salary_1(self, values):
        # Input data validation
        # Check required fields
        if not funcs.check_required_fields(values[2], values[3]):
            return Response(ResponseStatus.fail, strs.REQUIRED_FIELDS_NOT_FILLED_MSG)

        if not funcs.convert_to_int(values, [2, 3]):
            return Response(ResponseStatus.fail, strs.NOT_INTEGER_MSG)

        if values[2] < 0 or values[3] < 0:
            # TODO write to log
            return Response(ResponseStatus.fail, strs.INVALID_MEASURE_MSG)

        if values[2] > values[3]:
            return Response(ResponseStatus.fail, strs.INVALID_NET_GROSS_RATIO_MSG)

        return self._database_manager.actions(Actions.update_salary_1, values)

    def _update_salary_2(self, values):
        # Input data validation
        if not funcs.convert_to_int(values, [3, 5, 7, 9, 10, 11, 12]):
            return Response(ResponseStatus.fail, strs.NOT_INTEGER_MSG)

        if values[3] < 0 or values[5] < 0 or values[7] < 0 or values[9] < 0 \
                or values[10] < 0 or values[11] < 0 or values[12] < 0:
            # TODO write to log
            return Response(ResponseStatus.fail, strs.INVALID_MEASURE_MSG)

        return self._database_manager.actions(Actions.update_salary_2, values)

    def _delete_employee(self, values):
        response = self._database_manager.actions(Actions.delete_employee, values)

        if response.get_status() == ResponseStatus.success:
            for employee in self._employees:
                if employee.get_employee_id() == values[0]:
                    self._employees.remove(employee)
                    break

        return response

    def _delete_position(self, values):
        position_id = self._get_position_id(values[0])

        if position_id is None:
            return Response(ResponseStatus.fail, strs.INTERNAL_ERROR_MSG)

        values[0] = position_id
        response = self._database_manager.actions(Actions.delete_position, values)

        if response.get_status() == ResponseStatus.success:
            for position in self._positions:
                if position.get_position_id() == position_id:
                    self._positions.remove(position)
                    break

        return response

    def _delete_child(self, values):
        response = self._database_manager.actions(Actions.delete_child, values)

        if response.get_status() == ResponseStatus.success:
            for child in self._children:
                if child.get_child_id() == values[0]:
                    self._children.remove(child)
                    break

        return response

    def _delete_uniform(self, values):
        uniform_id = self._get_uniform_id(values[0])

        if uniform_id is None:
            # TODO Write to log
            return Response(ResponseStatus.fail, strs.INTERNAL_ERROR_MSG)

        values[0] = uniform_id

        response = self._database_manager.actions(Actions.delete_uniform, values)

        if response.get_status() == ResponseStatus.success:
            for uniform in self._uniforms:
                if uniform.get_uniform_id() == uniform_id:
                    self._uniforms.remove(uniform)
                    break

        return response

    def _delete_uniform_piece(self, values):
        response = self._database_manager.actions(Actions.delete_uniform_piece, values)

        if response.get_status() == ResponseStatus.success:
            for uniform_piece in self._uniform_pieces:
                if uniform_piece.get_uniform_piece_id() == values[0]:
                    self._uniform_pieces.remove(uniform_piece)
                    break

        return response

    def _delete_free_days(self, values):
        response = self._database_manager.actions(Actions.delete_free_days, values)

        if response.get_status() == ResponseStatus.success:
            for free_days in self._all_free_days:
                if free_days.get_free_days_id() == values[0]:
                    self._all_free_days.remove(free_days)
                    break

        return response

    def _delete_wage(self, values):
        response = self._database_manager.actions(Actions.delete_wage, values)

        if response.get_status() == ResponseStatus.success:
            for wage in self._wages:
                if wage.get_wage_id() == values[0]:
                    self._wages.remove(wage)
                    break

        return response

    def _delete_salary_1(self, values):
        return self._database_manager.actions(Actions.delete_salary_1, values)

    def _delete_salary_2(self, values):
        return self._database_manager.actions(Actions.delete_salary_2, values)
