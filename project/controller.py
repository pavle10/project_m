import sys
from PyQt5.QtWidgets import QApplication

from project.views.view_manager import ViewManager
from project.actions.action_manager import ActionManager
from project.utils.enums import Actions, Responses


class Controller:

    def __init__(self):
        self._app = QApplication(sys.argv)

        self._action_manager = ActionManager(self)

        self._init_models()

        self._view_manager = ViewManager(self)

    def _init_models(self):
        self._user = None
        self._employees = self._action_manager.actions(Actions.all_employees)
        self._positions = self._action_manager.actions(Actions.all_positions)
        self._uniforms = self._action_manager.actions(Actions.all_uniforms)
        self._uniform_pieces = self._action_manager.actions(Actions.all_uniform_pieces)
        self._children = self._action_manager.actions(Actions.all_children)
        self._all_free_days = self._action_manager.actions(Actions.all_free_days)
        self._wages = self._action_manager.actions(Actions.all_wages)

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
        elif action == Actions.all_uniforms:
            return self._get_all_uniforms()
        elif action == Actions.employee_salaries_2:
            return self._get_employee_salaries_2(values)
        elif action == Actions.delete_salary_2:
            return self._delete_salary_2(values)

    def _login(self, values):
        self._action_manager.actions(Actions.login, values)

        return Responses.success if self._user else Responses.fail

    def _add_position(self, values):
        response = self._action_manager.actions(Actions.add_position, values)

        if response:
            self._positions.append(response)
            return Responses.success

        return Responses.fail

    def _add_employee(self, values):
        position_id = self._get_position_id(values[6])

        if position_id is not None:
            values[6] = position_id
            response = self._action_manager.actions(Actions.add_employee, values)

            if response:
                self._employees.append(response)
                return Responses.success

        return Responses.fail

    def _add_uniform(self, values):
        response = self._action_manager.actions(Actions.add_uniform, values)

        if response:
            self._uniforms.append(response)
            return Responses.success

        return Responses.fail

    def _add_uniform_piece(self, values):
        uniform_id = self._get_uniform_id(values[0])
        employee_id = self._get_employee_id(values[1])

        if uniform_id is not None and employee_id is not None:
            values[0] = uniform_id
            values[1] = employee_id

            response = self._action_manager.actions(Actions.add_uniform_piece, values)

            if response:
                self._uniform_pieces.append(response)
                return Responses.success

        return Responses.fail

    def _add_child(self, values):
        mother_id = self._get_employee_id(values[2])
        father_id = self._get_employee_id(values[3])

        if not (mother_id is None and father_id is None):
            values[2] = mother_id
            values[3] = father_id

            response = self._action_manager.actions(Actions.add_child, values)

            if response:
                self._children.append(response)
                return Responses.success

        return Responses.fail

    def _add_free_days(self, values):
        employee_id = self._get_employee_id(values[0])

        if employee_id is not None:
            values[0] = employee_id

            response = self._action_manager.actions(Actions.add_free_days, values)

            if response:
                self._all_free_days.append(response)
                return Responses.success

        return Responses.fail

    def _add_wage(self, values):
        employee_id = self._get_employee_id(values[0])

        if employee_id is not None:
            values[0] = employee_id

            response = self._action_manager.actions(Actions.add_wage, values)

            if response:
                self._wages.append(response)
                return Responses.success

        return Responses.fail

    def _add_salary_1(self, values):
        employee_id = self._get_employee_id(values[0])

        if employee_id is not None:
            values[0] = employee_id

            response = self._action_manager.actions(Actions.add_salary_1, values)

            if response:
                return Responses.success

        return Responses.fail

    def _add_salary_2(self, values):
        employee_id = self._get_employee_id(values[0])

        if employee_id is None:
            return Responses.fail

        wage = self._get_employee_wage(employee_id)

        if wage is None:
            return Responses.fail

        values[0] = employee_id
        values[3] = wage.get_day()
        values[5] = wage.get_hour()
        values[7] = wage.get_meal()

        response = self._action_manager.actions(Actions.add_salary_2, values)

        if response:
            return Responses.success

        return Responses.fail

    def _get_all_positions(self):
        return [position.get_name() for position in self._positions]

    def _get_position_id(self, name):
        for position in self._positions:
            if position.name == name:
                return position.position_id

        return None

    def _get_all_employees(self):
        return [(employee.get_first_name(), employee.get_last_name(), employee.get_identity_number())
                for employee in self._employees]

    def _get_employee_id(self, value):
        values = value.split(' ')

        if len(values) != 3:
            return None

        identity_number = values[2]

        for employee in self._employees:
            if employee.get_identity_number() == identity_number:
                return employee.get_employee_id()

        return None

    def _get_all_uniforms(self):
        return [uniform.get_name() for uniform in self._uniforms]

    def _get_uniform_id(self, name):
        for uniform in self._uniforms:
            if uniform.get_name() == name:
                return uniform.get_uniform_id()

        return None

    def _get_employee_wage(self, employee_id):
        for wage in self._wages:
            if wage.get_employee_id() == employee_id:
                return wage

        return None

    def _get_employee_salaries_2(self, values):
        employee_id = self._get_employee_id(values[0])

        if employee_id is not None:
            values[0] = employee_id

            response = self._action_manager.actions(Actions.employee_salaries_2, values)

            if response:
                return response

        return Responses.fail

    def _delete_salary_2(self, values):
        response = self._action_manager.actions(Actions.delete_salary_2, values)

        return Responses.success if not response.endswith('0') else Responses.fail
