from project.database.database_manager import DatabaseManager
from project.enums.actions import Actions
from project.user import User


class ActionManager:

    def __init__(self, controller):
        self.controller = controller
        self._database_manager = DatabaseManager(self)

    def login_action(self, username, password):
        res = self._database_manager.actions(Actions.login, [username, password])

        if res:
            new_user = User(res[0], res[1])
            self.controller.set_user(new_user)
