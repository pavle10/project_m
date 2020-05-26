from PyQt5.QtWidgets import *

from project.utils.enums import Actions, Responses
from project.utils import funcs, strings as strs


class AddWageView(QWidget):

    def __init__(self, manager, *args, **kwargs):
        super(AddWageView, self).__init__(*args, **kwargs)

        self._manager = manager

        self._init_ui()

    def _init_ui(self):
        employee_label = QLabel(self)
        employee_label.setText(f"*{strs.EMPLOYEE}:")
        self.employee_box = QComboBox()
        for index, employee in enumerate(self._get_employees()):
            self.employee_box.insertItem(index, funcs.employee_unique_name(employee))
        employee_label.setBuddy(self.employee_box)

        day_label = QLabel(self)
        day_label.setText(f"*{strs.PRESENT_WAGE_HDR[0]}:")
        self.day_line = QLineEdit(self)
        day_label.setBuddy(self.day_line)

        hour_label = QLabel(self)
        hour_label.setText(f"*{strs.PRESENT_WAGE_HDR[1]}:")
        self.hour_line = QLineEdit(self)
        hour_label.setBuddy(self.hour_line)

        meal_label = QLabel(self)
        meal_label.setText(f"*{strs.PRESENT_WAGE_HDR[2]}:")
        self.meal_line = QLineEdit(self)
        meal_label.setBuddy(self.meal_line)

        add_button = QPushButton(self)
        add_button.setText(strs.ADD_BTN)
        add_button.clicked.connect(self._add_wage)

        layout = QFormLayout()
        layout.addRow(employee_label, self.employee_box)
        layout.addRow(day_label, self.day_line)
        layout.addRow(hour_label, self.hour_line)
        layout.addRow(meal_label, self.meal_line)
        layout.addWidget(add_button)
        self.setLayout(layout)

    def _get_employees(self):
        return self._manager.actions(Actions.all_employees)

    def _add_wage(self):
        values = [self.employee_box.currentText(), self.day_line.text(), self.hour_line.text(), self.meal_line.text()]

        response = self._manager.actions(Actions.add_wage, values)

        if response == Responses.success:
            QMessageBox.information(self, strs.ADD_VIEW_MSG, strs.WAGE_ADD_SUCC_MSG)
        elif response == Responses.fail:
            QMessageBox.warning(self, strs.ADD_VIEW_MSG, strs.WAGE_ADD_FAIL_MSG)


