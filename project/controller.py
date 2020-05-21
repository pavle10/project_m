import sys
from PyQt5.QtWidgets import QApplication

from project.views.view_manager import ViewManager
from project.actions.action_manager import ActionManager
from project.enums.responses import Responses
from project.enums.actions import Actions


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
        elif action == Actions.all_positions:
            return self._get_all_positions()

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

    def _get_all_positions(self):
        return [position.name for position in self._positions]

    def _get_position_id(self, name):
        for position in self._positions:
            if position.name == name:
                return position.position_id

        return None
