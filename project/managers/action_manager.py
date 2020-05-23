from project.managers.database_manager import DatabaseManager
from project.utils.enums import Actions
from project.models.user import User
from project.models.position import Position
from project.models.employee import Employee
from project.models.uniform import Uniform
from project.models.uniform_piece import UniformPiece
from project.models.child import Child
from project.models.free_days import FreeDays
from project.models.wage import Wage
from project.models.salaries import Salary1, Salary2


class ActionManager:

    def __init__(self, controller):
        self.controller = controller
        self._database_manager = DatabaseManager(self)

    def actions(self, action, values=None):
        if action == Actions.login:
            self._login(values)
        elif action == Actions.all_employees:
            return self._init_model(Actions.all_employees)
        elif action == Actions.all_positions:
            return self._init_model(Actions.all_positions)
        elif action == Actions.all_uniforms:
            return self._init_model(Actions.all_uniforms)
        elif action == Actions.all_uniform_pieces:
            return self._init_model(Actions.all_uniform_pieces)
        elif action == Actions.all_children:
            return self._init_model(Actions.all_children)
        elif action == Actions.all_free_days:
            return self._init_model(Actions.all_free_days)
        elif action == Actions.all_wages:
            return self._init_model(Actions.all_wages)
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
        elif action == Actions.employee_salaries_2:
            return self._get_employee_salaries_2(values)
        elif action == Actions.delete_salary_2:
            return self._delete_salary_2(values)

    def _login(self, values):
        res = self._database_manager.actions(Actions.login, values)

        if isinstance(res, tuple):
            new_user = User(res[0], res[1])
            self.controller.set_user(new_user)

    def _init_model(self, action):
        return self._database_manager.actions(action)

    def _add_position(self, values):
        result = self._database_manager.actions(Actions.add_position, values)

        return Position(result[0], result[1], result[2]) if result else None

    def _add_employee(self, values):
        result = self._database_manager.actions(Actions.add_employee, values)

        if result is None:
            return result

        new_employee = Employee(result[0], result[1], result[2], result[3], result[4],
                                result[5], result[6], result[7], result[8], result[9],
                                result[10], result[11], result[12], result[13], result[14], result[15])

        return new_employee

    def _add_uniform(self, values):
        result = self._database_manager.actions(Actions.add_uniform, values)

        return Uniform(result[0], result[1]) if result else None

    def _add_uniform_piece(self, values):
        result = self._database_manager.actions(Actions.add_uniform_piece, values)

        if result is None:
            return result

        new_uniform_piece = UniformPiece(result[0], result[1], result[2], result[3], result[4], result[5], result[6])

        return new_uniform_piece

    def _add_child(self, values):
        result = self._database_manager.actions(Actions.add_child, values)

        return Child(result[0], result[1], result[2], result[3], result[4]) if result else None

    def _add_free_days(self, values):
        result = self._database_manager.actions(Actions.add_free_days, values)

        return FreeDays(result[0], result[1], result[2], result[3], result[4], result[5]) if result else None

    def _add_wage(self, values):
        result = self._database_manager.actions(Actions.add_wage, values)

        return Wage(result[0], result[1], result[2], result[3], result[4]) if result else None

    def _add_salary_1(self, values):
        result = self._database_manager.actions(Actions.add_salary_1, values)

        return Salary1(result[0], result[1], result[2], result[3], result[4]) if result else None

    def _add_salary_2(self, values):
        result = self._database_manager.actions(Actions.add_salary_2, values)

        if result is None:
            return result

        new_salary = Salary2(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7],
                             result[8], result[9], result[10], result[11], result[12])

        return new_salary

    def _get_employee_salaries_2(self, values):
        result = self._database_manager.actions(Actions.employee_salaries_2, values)

        if isinstance(result, tuple):
            result = [result]

        return result

    def _delete_salary_2(self, values):
        result = self._database_manager.actions(Actions.delete_salary_2, values)

        return result

