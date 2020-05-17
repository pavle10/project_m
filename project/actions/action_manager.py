from project.database.database_manager import DatabaseManager
from project.enums.actions import Actions
from project.models.user import User
from project.models.position import Position
from project.models.employee import Employee


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
        elif action == Actions.add_position:
            return self._add_position(values)
        elif action == Actions.add_employee:
            return self._add_employee(values)

    def _login(self, values):
        res = self._database_manager.actions(Actions.login, values)

        if res:
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
