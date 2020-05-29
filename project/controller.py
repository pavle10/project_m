import sys
from PyQt5.QtWidgets import QApplication

from project.managers.database_manager import DatabaseManager
from project.managers.view_manager import ViewManager
from project.managers.action_manager import ActionManager
from project.utils.enums import Actions, ResponseStatus
from project.models.user import User
from project.models.response import Response
from project.utils import funcs, strings as strs


class Controller:

    def __init__(self):
        self._app = QApplication(sys.argv)

        self._database_manager = DatabaseManager()

        self._action_manager = ActionManager()

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

    def run(self):
        self._view_manager.actions(Actions.show)

        return self._app.exec_()

    def set_user(self, user):
        self._user = user

    def get_username(self):
        return self._user.get_username()

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
            return self._get_employee_wage(self._get_employee_id(values[0]))
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

    def _update_uniform_pieces_name(self):
        for piece in self._uniform_pieces:
            for uniform in self._uniforms:
                if uniform.get_uniform_id() == piece.get_uniform_id():
                    piece.set_uniform_name(uniform.get_name())
                    break

    def _update_children_parents(self):
        for child in self._children:
            mother_id = child.get_mother_id()
            father_id = child.get_father_id()

            for employee in self._employees:
                if employee.get_employee_id() == mother_id:
                    child.set_mother_name(funcs.employee_unique_name(employee))
                elif employee.get_employee_id() == father_id:
                    child.set_father_name(funcs.employee_unique_name(employee))

    def _login(self, values):
        # Input data validation
        if values[0] == "" or values[1] == "":
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
            self._positions.append(response)

        return response

    def _add_employee(self, values):
        # Input data validation
        # Check required fields
        if not funcs.check_required_fields(values[0], values[1], values[3], values[6], values[8]):
            return Response(ResponseStatus.fail, strs.REQUIRED_FIELDS_NOT_FILLED_MSG)

        # Check before m fields
        before_m = values[10]

        try:
            years = 0 if before_m[0] == "" else int(before_m[0])
            months = 0 if before_m[1] == "" else int(before_m[1])
            days = 0 if before_m[2] == "" else int(before_m[2])
        except ValueError:
            # TODO write to log
            return Response(ResponseStatus.fail, strs.NOT_INTEGER_VALUE_MSG.format(field=strs.PRESENT_EMPLOYEE_HDR[10]))

        if years < 0 or months < 0 or months > 11 or days < 0 or days > 30:
            # TODO write to log
            return Response(ResponseStatus.fail, strs.INVALID_DATE_FORMAT)

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
        response = self._action_manager.actions(Actions.add_uniform, values)

        if response:
            self._uniforms.append(response)
            return ResponseStatus.success

        return ResponseStatus.fail

    def _add_uniform_piece(self, values):
        uniform_id = self._get_uniform_id(values[0])
        employee_id = self._get_employee_id(values[1])

        if uniform_id is not None and employee_id is not None:
            values[0] = uniform_id
            values[1] = employee_id

            response = self._action_manager.actions(Actions.add_uniform_piece, values)

            if response:
                self._uniform_pieces.append(response)
                return ResponseStatus.success

        return ResponseStatus.fail

    def _add_child(self, values):
        # Input data validation
        # Check required fields
        if not funcs.check_required_fields(values[0], values[1], values[3]):
            return Response(ResponseStatus.fail, strs.REQUIRED_FIELDS_NOT_FILLED_MSG)

        mother_id = self._get_employee_id(values[4])
        father_id = self._get_employee_id(values[5])

        if mother_id is None and father_id is None:
            return Response(ResponseStatus.fail, strs.CHILD_ONE_PARENT_REQUIRED)

        values[4] = mother_id
        values[5] = father_id

        response = self._database_manager.actions(Actions.add_child, values)

        if response.get_status() == ResponseStatus.success:
            self._children.append(response.get_data())

        return response

    def _add_free_days(self, values):
        employee_id = self._get_employee_id(values[0])

        if employee_id is not None:
            values[0] = employee_id

            response = self._action_manager.actions(Actions.add_free_days, values)

            if response:
                self._all_free_days.append(response)
                return ResponseStatus.success

        return ResponseStatus.fail

    def _add_wage(self, values):
        employee_id = self._get_employee_id(values[0])

        if employee_id is not None:
            values[0] = employee_id

            response = self._action_manager.actions(Actions.add_wage, values)

            if response:
                self._wages.append(response)
                return ResponseStatus.success

        return ResponseStatus.fail

    def _add_salary_1(self, values):
        employee_id = self._get_employee_id(values[0])

        if employee_id is not None:
            values[0] = employee_id

            response = self._action_manager.actions(Actions.add_salary_1, values)

            if response:
                return ResponseStatus.success

        return ResponseStatus.fail

    def _add_salary_2(self, values):
        employee_id = self._get_employee_id(values[0])

        if employee_id is None:
            return ResponseStatus.fail

        wage = self._get_employee_wage(employee_id)

        if wage is None:
            return ResponseStatus.fail

        values[0] = employee_id
        values[3] = wage.get_day()
        values[5] = wage.get_hour()
        values[7] = wage.get_meal()

        response = self._action_manager.actions(Actions.add_salary_2, values)

        if response:
            return ResponseStatus.success

        return ResponseStatus.fail

    def _get_all_positions(self):
        return self._positions

    def _get_position_id(self, name):
        for position in self._positions:
            if position.get_name() == name:
                return position.get_position_id()

        return None

    def _get_all_employees(self):
        return self._employees

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
        employee_id = self._get_employee_id(values[0])
        result = list()

        if employee_id is not None:
            start_date = values[1]
            end_date = values[2]

            for piece in self._uniform_pieces:
                if piece.get_employee_id() == employee_id and start_date <= piece.get_date() <= end_date:
                    result.append(piece)

        return result

    def _get_employee_free_days(self, values):
        employee_id = self._get_employee_id(values[0])
        result = list()

        if employee_id is not None:
            start_date = values[1]
            end_date = values[2]

            for free_days in self._all_free_days:
                if free_days.get_employee_id() == employee_id \
                        and start_date <= free_days.get_start_date() \
                        and free_days.get_end_date() <= end_date:
                    result.append(free_days)

        return result

    def _get_employee_wage(self, employee_id):
        for wage in self._wages:
            if wage.get_employee_id() == employee_id:
                return wage

        return None

    def _get_employee_salaries_1(self, values):
        employee_id = self._get_employee_id(values[0][0])

        if employee_id is not None:
            values[0][0] = employee_id
            start_date = values[1]
            end_date = values[2]

            response = self._action_manager.actions(Actions.employee_salaries_1, values[0])

            if response:
                return [salary for salary in response if start_date <= salary[4] <= end_date]

        return None

    def _get_employee_salaries_2(self, values):
        employee_id = self._get_employee_id(values[0][0])

        if employee_id is not None:
            values[0][0] = employee_id
            start_date = values[1]
            end_date = values[2]

            response = self._action_manager.actions(Actions.employee_salaries_2, values[0])

            if response:
                return [salary for salary in response if start_date <= salary[2] <= end_date]

        return None

    def _update_employee(self, values):
        position_id = self._get_position_id(values[7])

        print(position_id)

        if position_id is not None:
            values[7] = position_id
            values[11] = 0 if values[11] == "" else values[11]
            response = self._action_manager.actions(Actions.update_employee, values)

            if not response.endswith('0'):
                for employee in self._employees:
                    if employee.get_employee_id() == values[0]:
                        employee.set_first_name(values[1])
                        employee.set_last_name(values[2])
                        employee.set_fathers_name(values[3])
                        employee.set_identity_number(values[4])
                        employee.set_personal_card(values[5])
                        employee.set_qualification(values[6])
                        employee.set_position(values[7])
                        employee.set_saint_day(values[8])
                        employee.set_address(values[9])
                        employee.set_account(values[10])
                        employee.set_before_m(values[11])
                        employee.set_start_date(values[12])
                        employee.set_home_number(values[13])
                        employee.set_mobile_number(values[14])
                        employee.set_situation(values[15])

                        return ResponseStatus.success

        return ResponseStatus.fail

    def _update_position(self, values):
        position_id = self._get_position_id(values[0])

        if position_id is not None:
            values[1][0] = position_id
            response = self._action_manager.actions(Actions.update_position, values[1])

            if not response.endswith('0'):
                for position in self._positions:
                    if position.get_name() == values[0]:
                        position.set_name(values[1][1])
                        position.set_saturday(values[1][2])

                        return ResponseStatus.success

        return ResponseStatus.fail

    def _update_child(self, values):
        mother_id = self._get_employee_id(values[4])
        father_id = self._get_employee_id(values[6])
        query_values = [values[0], values[1], values[2], mother_id, father_id]

        response = self._action_manager.actions(Actions.update_child, query_values)

        if not response.endswith('0'):
            for child in self._children:
                if child.get_child_id() == values[0]:
                    child.set_identity_number(values[1])
                    child.set_birth_year(values[2])
                    child.set_mother_id(mother_id)
                    child.set_mother_name(values[4])
                    child.set_father_id(father_id)
                    child.set_father_name(values[6])

                    return ResponseStatus.success

        return ResponseStatus.fail

    def _update_uniform(self, values):
        uniform_id = self._get_uniform_id(values[0])

        if uniform_id is not None:
            values[0] = uniform_id
            response = self._action_manager.actions(Actions.update_uniform, values)

            if not response.endswith('0'):
                for uniform in self._uniforms:
                    if uniform.get_uniform_id() == uniform_id:
                        uniform.set_name(values[1])

                        return ResponseStatus.success

        return ResponseStatus.fail

    def _update_uniform_piece(self, values):
        response = self._action_manager.actions(Actions.update_uniform_piece, values)

        if not response.endswith('0'):
            for uniform_piece in self._uniform_pieces:
                if uniform_piece.get_uniform_piece_id() == values[0]:
                    uniform_piece.set_uniform_id(values[1])
                    uniform_piece.set_uniform_name(self._get_uniform_name(values[1]))
                    uniform_piece.set_size(values[3])
                    uniform_piece.set_quantity(values[4])
                    uniform_piece.set_additional(values[5])
                    uniform_piece.set_date(values[6])

                    return ResponseStatus.success

        return ResponseStatus.fail

    def _update_free_days(self, values):
        response = self._action_manager.actions(Actions.update_free_days, values)

        if not response.endswith('0'):
            for free_days in self._all_free_days:
                if free_days.get_free_days_id() == values[0]:
                    free_days.set_start_date(values[2])
                    free_days.set_end_date(values[3])
                    free_days.set_total_days(values[4])
                    free_days.set_reason(values[5])

                    return ResponseStatus.success

        return ResponseStatus.fail

    def _update_wage(self, values):
        response = self._action_manager.actions(Actions.update_wage, values)

        if not response.endswith('0'):
            for wage in self._wages:
                if wage.get_wage_id() == values[0]:
                    wage.set_day(values[2])
                    wage.set_hour(values[3])
                    wage.set_meal(values[4])

                    return ResponseStatus.success

        return ResponseStatus.fail

    def _update_salary_1(self, values):
        response = self._action_manager.actions(Actions.update_salary_1, values)

        return ResponseStatus.success if not response.endswith('0') else ResponseStatus.fail

    def _update_salary_2(self, values):
        response = self._action_manager.actions(Actions.update_salary_2, values)

        return ResponseStatus.success if not response.endswith('0') else ResponseStatus.fail

    def _delete_employee(self, values):
        response = self._action_manager.actions(Actions.delete_employee, values)

        if not response.endswith('0'):
            for employee in self._employees:
                if employee.get_employee_id() == values[0]:
                    self._employees.remove(employee)

                    return ResponseStatus.success

        return ResponseStatus.fail

    def _delete_position(self, values):
        position_id = self._get_position_id(values[0])

        if position_id is not None:
            values[0] = position_id
            response = self._action_manager.actions(Actions.delete_position, values)
            print(response)

            if not response.endswith('0'):
                for position in self._positions:
                    if position.get_position_id() == position_id:
                        self._positions.remove(position)

                        return ResponseStatus.success

        return ResponseStatus.fail

    def _delete_child(self, values):
        response = self._action_manager.actions(Actions.delete_child, values)

        if not response.endswith('0'):
            for child in self._children:
                if child.get_child_id() == values[0]:
                    self._children.remove(child)

                    return ResponseStatus.success

        return ResponseStatus.fail

    def _delete_uniform(self, values):
        uniform_id = self._get_uniform_id(values[0])

        if uniform_id is not None:
            values[0] = uniform_id

            response = self._action_manager.actions(Actions.delete_uniform, values)

            if not response.endswith('0'):
                for uniform in self._uniforms:
                    if uniform.get_uniform_id() == uniform_id:
                        self._uniforms.remove(uniform)

                        return ResponseStatus.success

        return ResponseStatus.fail

    def _delete_uniform_piece(self, values):
        response = self._action_manager.actions(Actions.delete_uniform_piece, values)

        if not response.endswith('0'):
            for uniform_piece in self._uniform_pieces:
                if uniform_piece.get_uniform_piece_id() == values[0]:
                    self._uniform_pieces.remove(uniform_piece)

                    return ResponseStatus.success

        return ResponseStatus.fail

    def _delete_free_days(self, values):
        response = self._action_manager.actions(Actions.delete_free_days, values)

        if not response.endswith('0'):
            for free_days in self._all_free_days:
                if free_days.get_free_days_id() == values[0]:
                    self._all_free_days.remove(free_days)

                    return ResponseStatus.success

        return ResponseStatus.fail

    def _delete_wage(self, values):
        response = self._action_manager.actions(Actions.delete_wage, [values[0]])

        if not response.endswith('0'):
            self._wages.remove(self._get_employee_wage(values[1]))

            return ResponseStatus.success

        return ResponseStatus.fail

    def _delete_salary_1(self, values):
        response = self._action_manager.actions(Actions.delete_salary_1, values)

        return ResponseStatus.success if not response.endswith('0') else ResponseStatus.fail

    def _delete_salary_2(self, values):
        response = self._action_manager.actions(Actions.delete_salary_2, values)

        return ResponseStatus.success if not response.endswith('0') else ResponseStatus.fail
