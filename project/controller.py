import sys
from PyQt5.QtWidgets import QApplication

from project.views.view_manager import ViewManager
from project.actions.action_manager import ActionManager
from project.enums.responses import Responses
from project.enums.actions import Actions


class Controller:

    def __init__(self):
        self._app = QApplication(sys.argv)

        self._view_manager = ViewManager(self)
        self._action_manager = ActionManager(self)

        self._init_models()

    def _init_models(self):
        self._user = None
        self._employees = self._action_manager.actions(Actions.init_employees)
        self._positions = self._action_manager.actions(Actions.init_positions)

        print(f"Positions count: {len(self._positions)}")
        print(self._positions)

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

    def _login(self, values):
        self._action_manager.actions(Actions.login, values)

        return Responses.success if self._user else Responses.fail

    def _add_position(self, values):
        response = self._action_manager.actions(Actions.add_position, values)

        if response:
            self._positions.append(response)
            return Responses.success
        return Responses.fail
