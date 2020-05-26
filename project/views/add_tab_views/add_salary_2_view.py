import datetime
from PyQt5.QtWidgets import *

from project.utils.enums import Actions, Responses
from project.utils import funcs as funcs, strings as strs, constants as cons


class AddSalary2View(QWidget):

    def __init__(self, manager, *args, **kwargs):
        super(AddSalary2View, self).__init__(*args, **kwargs)

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
        day_label.setText(f"*{strs.PRESENT_SALARY_2_HDR[1]}:")
        self.day_line = QLineEdit(self)
        day_label.setBuddy(self.day_line)

        hour_label = QLabel(self)
        hour_label.setText(f"*{strs.PRESENT_SALARY_2_HDR[3]}:")
        self.hour_line = QLineEdit(self)
        hour_label.setBuddy(self.hour_line)

        meal_label = QLabel(self)
        meal_label.setText(f"*{strs.PRESENT_SALARY_2_HDR[5]}:")
        self.meal_line = QLineEdit(self)
        meal_label.setBuddy(self.meal_line)

        payment_label = QLabel(self)
        payment_label.setText(f"*{strs.PRESENT_SALARY_2_HDR[7]}:")
        self.payment_line = QLineEdit(self)
        payment_label.setBuddy(self.payment_line)

        vacation_label = QLabel(self)
        vacation_label.setText(f"*{strs.PRESENT_SALARY_2_HDR[8]}:")
        self.vacation_line = QLineEdit(self)
        vacation_label.setBuddy(self.vacation_line)

        vacation_value_label = QLabel(self)
        vacation_value_label.setText(f"*{strs.PRESENT_SALARY_2_HDR[9]}:")
        self.vacation_value_line = QLineEdit(self)
        vacation_value_label.setBuddy(self.vacation_value_line)

        fix_label = QLabel(self)
        fix_label.setText(f"*{strs.PRESENT_SALARY_2_HDR[10]}:")
        self.fix_line = QLineEdit(self)
        fix_label.setBuddy(self.fix_line)

        date_label = QLabel(self)
        date_label.setText(f"*{strs.PRESENT_SALARY_2_HDR[0]}:")
        self.date_line = QDateEdit(self)
        self.date_line.setDate(datetime.datetime.now().date())
        self.date_line.setDisplayFormat(cons.DATE_FORMAT_PYQT)
        date_label.setBuddy(self.date_line)

        add_button = QPushButton(self)
        add_button.setText(strs.ADD_BTN)
        add_button.clicked.connect(self._add_salary)

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

    def _add_salary(self):
        chosen_date = self.date_line.date().toPyDate()
        values = [self.employee_box.currentText(), chosen_date, self.day_line.text(), None, self.hour_line.text(),
                  None, self.meal_line.text(), None, self.payment_line.text(), self.vacation_line.text(),
                  self.vacation_value_line.text(), self.fix_line.text()]

        response = self._manager.actions(Actions.add_salary_2, values)

        if response == Responses.success:
            QMessageBox.information(self, strs.ADD_VIEW_MSG, strs.SALARY_2_ADD_SUCC_MSG)
        elif response == Responses.fail:
            QMessageBox.warning(self, strs.ADD_VIEW_MSG, strs.SALARY_2_ADD_FAIL_MSG)
