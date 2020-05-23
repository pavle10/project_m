from project.views.login_view import LoginView
from project.views.main_window_view import MainWind
from project.utils.enums import Actions, Responses


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
        elif action == Actions.add_uniform:
            return self._add_uniform(values)
        elif action == Actions.add_uniform_piece:
            return self._add_uniform_piece(values)
        elif action == Actions.add_child:
            return self._add_child(values)
        elif action == Actions.add_free_days:
            return self._add_free_days(values)
        elif action == Actions.add_wage:
            return self._add_wage(values)
        elif action == Actions.add_salary_1:
            return self._add_salary_1(values)
        elif action == Actions.add_salary_2:
            return self._add_salary_2(values)
        elif action == Actions.all_positions:
            return self._get_all_positions()
        elif action == Actions.all_employees:
            return self._get_all_employees()
        elif action == Actions.all_uniforms:
            return self._get_all_uniforms()
        elif action == Actions.employee_salaries_2:
            return self._get_employee_salaries_2(values)
        elif action == Actions.delete_salary_2:
            return self._delete_salary_2(values)

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

    def _add_uniform(self, values):
        return self._controller.actions(Actions.add_uniform, values)

    def _add_uniform_piece(self, values):
        return self._controller.actions(Actions.add_uniform_piece, values)

    def _add_child(self, values):
        return self._controller.actions(Actions.add_child, values)

    def _add_free_days(self, values):
        return self._controller.actions(Actions.add_free_days, values)

    def _add_wage(self, values):
        return self._controller.actions(Actions.add_wage, values)

    def _add_salary_1(self, values):
        return self._controller.actions(Actions.add_salary_1, values)

    def _add_salary_2(self, values):
        return self._controller.actions(Actions.add_salary_2, values)

    def _get_all_positions(self):
        return self._controller.actions(Actions.all_positions)

    def _get_all_employees(self):
        return self._controller.actions(Actions.all_employees)

    def _get_all_uniforms(self):
        return self._controller.actions(Actions.all_uniforms)

    def _get_employee_salaries_2(self, values):
        return self._controller.actions(Actions.employee_salaries_2, values)

    def _delete_salary_2(self, values):
        return self._controller.actions(Actions.delete_salary_2, values)