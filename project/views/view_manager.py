from project.views.login_view import LoginView
from project.views.main_window import MainWind
from project.enums.responses import Responses


class ViewManager:

    def __init__(self, controller):
        self.controller = controller
        self.login = LoginView(self)
        self.main_wind = MainWind(self)

    def show_login(self):
        self.login.show()

    def login_action(self, username, password):
        response = self.controller.login(username, password)

        if response == Responses.success:
            self.login.successful_login(self.controller.get_username())
            self.login.close()
            self.main_wind.show()
        elif response == Responses.fail:
            self.login.failed_login()
