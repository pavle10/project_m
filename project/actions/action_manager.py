from project.database.database_manager import DatabaseManager
from project.enums.actions import Actions
from project.models.user import User
from project.models.position import Position


class ActionManager:

    def __init__(self, controller):
        self.controller = controller
        self._database_manager = DatabaseManager(self)

    def actions(self, action, values=None):
        if action == Actions.login:
            self._login(values)
        elif action == Actions.init_employees:
            return self._init_model(Actions.init_employees)
        elif action == Actions.init_positions:
            return self._init_model(Actions.init_positions)
        elif action == Actions.add_position:
            return self._add_position(values)

    def _login(self, values):
        res = self._database_manager.actions(Actions.login, values)

        if res:
            new_user = User(res[0], res[1])
            self.controller.set_user(new_user)

    def _init_model(self, action):
        result = self._database_manager.actions(action)

        return [Position(pos[0], pos[1], pos[2]) for pos in result]

    def _add_position(self, values):
        result = self._database_manager.actions(Actions.add_position, values)

        return Position(result[0], result[1], result[2]) if result else None
