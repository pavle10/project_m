from project.utils import funcs as funcs, strings as strs
from project.views.tab_view.add_tab_views.add_view import AddView
from project.utils.enums import Actions, ResponseStatus
from project.models.my_widgets import *


class AddSalary2View(AddView):

    def __init__(self, name, manager, *args, **kwargs):
        super(AddSalary2View, self).__init__(*args, **kwargs)
        self._name = name
        self._manager = manager

        self._init_ui()

    def _init_ui(self):
        employee_label = MyLabel(strs.EMPLOYEE, is_required=True)
        self.employee_box = MyComboBox()
        for index, employee in enumerate(self._get_employees()):
            self.employee_box.insertItem(index, funcs.employee_unique_name(employee))
        employee_label.setBuddy(self.employee_box)

        day_label = MyLabel(strs.PRESENT_SALARY_2_HDR[1], is_required=True)
        self.day_line = MyEditLine()
        day_label.setBuddy(self.day_line)

        hour_label = MyLabel(strs.PRESENT_SALARY_2_HDR[3], is_required=True)
        self.hour_line = MyEditLine()
        hour_label.setBuddy(self.hour_line)

        meal_label = MyLabel(strs.PRESENT_SALARY_2_HDR[5], is_required=True)
        self.meal_line = MyEditLine()
        meal_label.setBuddy(self.meal_line)

        payment_label = MyLabel(strs.PRESENT_SALARY_2_HDR[7], is_required=True)
        self.payment_line = MyEditLine()
        payment_label.setBuddy(self.payment_line)

        vacation_label = MyLabel(strs.PRESENT_SALARY_2_HDR[8], is_required=True)
        self.vacation_line = MyEditLine()
        vacation_label.setBuddy(self.vacation_line)

        vacation_value_label = MyLabel(strs.PRESENT_SALARY_2_HDR[9], is_required=True)
        self.vacation_value_line = MyEditLine()
        vacation_value_label.setBuddy(self.vacation_value_line)

        fix_label = MyLabel(strs.PRESENT_SALARY_2_HDR[10], is_required=True)
        self.fix_line = MyEditLine()
        fix_label.setBuddy(self.fix_line)

        date_label = MyLabel(strs.PRESENT_SALARY_2_HDR[0], is_required=True)
        self.date_line = MyEditDate()
        date_label.setBuddy(self.date_line)

        add_button = MyButton(strs.ADD_BTN)
        add_button.clicked.connect(self._add)

        layout = QFormLayout()
        layout.addRow(employee_label, self.employee_box)
        layout.addRow(day_label, self.day_line)
        layout.addRow(hour_label, self.hour_line)
        layout.addRow(meal_label, self.meal_line)
        layout.addRow(payment_label, self.payment_line)
        layout.addRow(vacation_label, self.vacation_line)
        layout.addRow(vacation_value_label, self.vacation_value_line)
        layout.addRow(fix_label, self.fix_line)
        layout.addRow(date_label, self.date_line)
        layout.addWidget(add_button)
        self.setLayout(layout)

    def _get_employees(self):
        return self._manager.actions(Actions.all_employees)

    def _add(self):
        chosen_date = self.date_line.date().toPyDate()
        values = [self.employee_box.currentText(), chosen_date, self.day_line.text(), None, self.hour_line.text(),
                  None, self.meal_line.text(), None, self.payment_line.text(), self.vacation_line.text(),
                  self.vacation_value_line.text(), self.fix_line.text()]

        response = self._manager.actions(Actions.add_salary_2, values)

        if response == ResponseStatus.success:
            QMessageBox.information(self, strs.ADD_VIEW_MSG, strs.SALARY_2_ADD_SUCC_MSG)
        elif response == ResponseStatus.fail:
            QMessageBox.warning(self, strs.ADD_VIEW_MSG, strs.SALARY_2_ADD_FAIL_MSG)

    def get_name(self):
        return self._name