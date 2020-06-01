from project.views.tab_view.add_tab_views.add_view import AddView
from project.utils.enums import Actions, ResponseStatus
from project.utils import funcs, strings as strs
from project.models.my_widgets import *


class AddWageView(AddView):

    def __init__(self, name, manager, *args, **kwargs):
        super(AddWageView, self).__init__(*args, **kwargs)
        self._name = name
        self._manager = manager

        self._init_ui()

    def _init_ui(self):
        employee_label = MyLabel(strs.EMPLOYEE, is_required=True)
        self.employee_box = MyComboBox(self._generate_items())
        employee_label.setBuddy(self.employee_box)

        day_label = MyLabel(strs.PRESENT_WAGE_HDR[1], is_required=True)
        self.day_line = MyEditLine()
        day_label.setBuddy(self.day_line)

        hour_label = MyLabel(strs.PRESENT_WAGE_HDR[2], is_required=True)
        self.hour_line = MyEditLine()
        hour_label.setBuddy(self.hour_line)

        meal_label = MyLabel(strs.PRESENT_WAGE_HDR[3], is_required=True)
        self.meal_line = MyEditLine()
        meal_label.setBuddy(self.meal_line)

        add_button = MyButton(strs.ADD_BTN)
        add_button.clicked.connect(self._add)

        layout = QFormLayout()
        layout.addRow(employee_label, self.employee_box)
        layout.addRow(day_label, self.day_line)
        layout.addRow(hour_label, self.hour_line)
        layout.addRow(meal_label, self.meal_line)
        layout.addWidget(add_button)
        self.setLayout(layout)

    def _generate_items(self):
        return [funcs.employee_unique_name(employee) for employee in self._get_employees()]

    def _get_employees(self):
        return self._manager.actions(Actions.all_employees)

    def _add(self):
        values = [self.employee_box.currentText(), self.day_line.text(), self.hour_line.text(), self.meal_line.text()]

        response = self._manager.actions(Actions.add_wage, values)

        funcs.show_message(self, response.get_status(), strs.ADD_VIEW_MSG, response.get_message())

        if response.get_status() == ResponseStatus.success:
            self._clear()

    def _clear(self):
        self.employee_box.setCurrentIndex(0)
        self.day_line.clear()
        self.hour_line.clear()
        self.meal_line.clear()

    def get_name(self):
        return self._name

    def update(self):
        self.employee_box.update_items(self._generate_items())

