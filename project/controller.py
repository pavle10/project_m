import sys
from PyQt5.QtWidgets import QApplication

from project.views.view_manager import ViewManager
from project.actions.action_manager import ActionManager
from project.enums.responses import Responses


class Controller:

    def __init__(self):
        self._app = QApplication(sys.argv)
        self._view_manager = ViewManager(self)
        self._action_manager = ActionManager(self)
        self._user = None

    def run(self):
        self._view_manager.show_login()

        return self._app.exec_()

    def login(self, username, password):
        self._action_manager.login_action(username, password)

        return Responses.success if self._user else Responses.fail

    def set_user(self, user):
        self._user = user

    def get_username(self):
        return self._user.get_username()
