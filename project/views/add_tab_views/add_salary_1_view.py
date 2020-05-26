import datetime
from PyQt5.QtWidgets import *

from project.utils.enums import Actions, Responses
from project.utils import funcs as funcs, strings as strs, constants as cons


class AddSalary1View(QWidget):

    def __init__(self, manager, *args, **kwargs):
        super(AddSalary1View, self).__init__(*args, **kwargs)

        self._manager = manager

        self._init_ui()

    def _init_ui(self):
        employee_label = QLabel(self)
        employee_label.setText(f"*{strs.EMPLOYEE}:")
        self.employee_box = QComboBox()
        for index, employee in enumerate(self._get_employees()):
            self.employee_box.insertItem(index, funcs.employee_unique_name(employee))
        employee_label.setBuddy(self.employee_box)

        net_label = QLabel(self)
        net_label.setText(f"*{strs.PRESENT_SALARY_1_HDR[0]}:")
        self.net_line = QLineEdit(self)
        net_label.setBuddy(self.net_line)

        gross_label = QLabel(self)
        gross_label.setText(f"*{strs.PRESENT_SALARY_1_HDR[1]}:")
        self.gross_line = QLineEdit(self)
        gross_label.setBuddy(self.gross_line)

        date_label = QLabel(self)
        date_label.setText(f"*{strs.PRESENT_SALARY_1_HDR[2]}:")
        self.date_line = QDateEdit(self)
        self.date_line.setDate(datetime.datetime.now().date())
        self.date_line.setDisplayFormat(cons.DATE_FORMAT_PYQT)
        date_label.setBuddy(self.date_line)

        add_button = QPushButton(self)
        add_button.setText(strs.ADD_BTN)
        add_button.clicked.connect(self._add_salary)

        layout = QFormLayout()
        layout.addRow(employee_label, self.employee_box)
        layout.addRow(net_label, self.net_line)
        layout.addRow(gross_label, self.gross_line)
        layout.addRow(date_label, self.date_line)
        layout.addWidget(add_button)
        self.setLayout(layout)

    def _get_employees(self):
        return self._manager.actions(Actions.all_employees)

    def _add_salary(self):
        chosen_date = self.date_line.date().toPyDate()
        values = [self.employee_box.currentText(), self.net_line.text(), self.gross_line.text(), chosen_date]

        response = self._manager.actions(Actions.add_salary_1, values)

        if response == Responses.success:
            QMessageBox.information(self, strs.ADD_VIEW_MSG, strs.SALARY_1_ADD_SUCC_MSG)
        elif response == Responses.fail:
            QMessageBox.warning(self, strs.ADD_VIEW_MSG, strs.SALARY_1_ADD_FAIL_MSG)
