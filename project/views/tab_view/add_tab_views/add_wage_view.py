from project.views.add_tab_views.add_view import AddView
from project.utils.enums import Actions, Responses
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
        self.employee_box = MyComboBox()
        for index, employee in enumerate(self._get_employees()):
            self.employee_box.insertItem(index, funcs.employee_unique_name(employee))
        employee_label.setBuddy(self.employee_box)

        day_label = MyLabel(strs.PRESENT_WAGE_HDR[0], is_required=True)
        self.day_line = MyEditLine()
        day_label.setBuddy(self.day_line)

        hour_label = MyLabel(strs.PRESENT_WAGE_HDR[1], is_required=True)
        self.hour_line = MyEditLine()
        hour_label.setBuddy(self.hour_line)

        meal_label = MyLabel(strs.PRESENT_WAGE_HDR[2], is_required=True)
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

    def _get_employees(self):
        return self._manager.actions(Actions.all_employees)

    def _add(self):
        values = [self.employee_box.currentText(), self.day_line.text(), self.hour_line.text(), self.meal_line.text()]

        response = self._manager.actions(Actions.add_wage, values)

        if response == Responses.success:
            QMessageBox.information(self, strs.ADD_VIEW_MSG, strs.WAGE_ADD_SUCC_MSG)
        elif response == Responses.fail:
            QMessageBox.warning(self, strs.ADD_VIEW_MSG, strs.WAGE_ADD_FAIL_MSG)

    def get_name(self):
        return self._name

