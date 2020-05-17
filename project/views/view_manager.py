from project.views.login_view import LoginView
from project.views.main_window import MainWind
from project.enums.responses import Responses
from project.enums.actions import Actions


class ViewManager:

    def __init__(self, controller):
        self._controller = controller
        self.login = LoginView(self)
        self.main_wind = MainWind(self)

    def actions(self, action, values=None):
        if action == Actions.show:
            self._show_login()
        elif action == Actions.login:
            self._login(values)
        elif action == Actions.add_position:
            return self._add_position(values)
        elif action == Actions.add_employee:
            return self._add_employee(values)
        elif action == Actions.all_positions:
            return self._get_all_positions()

    def _show_login(self):
        self.login.show()

    def _login(self, values):
        response = self._controller.actions(Actions.login, values)

        if response == Responses.success:
            self.login.successful_login(self._controller.get_username())
            self.login.close()
            self.main_wind.show()
        elif response == Responses.fail:
            self.login.failed_login()

    def _add_position(self, values):
        return self._controller.actions(Actions.add_position, values)

    def _add_employee(self, values):
        return self._controller.actions(Actions.add_employee, values)

    def _get_all_positions(self):
        return self._controller.actions(Actions.all_positions)
