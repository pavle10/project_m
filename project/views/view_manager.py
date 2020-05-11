from project.views.login_view import LoginView


class ViewManager:

    def __init__(self):
        self.login = LoginView()

    def show_login(self):
        self.login.show()
