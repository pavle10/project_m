import sys
from PyQt5.QtWidgets import QApplication
from project.views.view_manager import ViewManager
from project.actions.action_manager import ActionManager
from project.database.database_manager import DatabaseManager


class Controller:

    def __init__(self):
        self._app = QApplication(sys.argv)
        self._view_manager = ViewManager()
        self._action_manager = ActionManager()
        self._database_manager = DatabaseManager()

    def run(self):
        self._view_manager.show_login()

        return self._app.exec_()
