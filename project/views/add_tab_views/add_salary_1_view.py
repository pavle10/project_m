from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from project.utils.enums import Actions, Responses
import project.utils.funcs as funcs


class AddSalary1View(QWidget):

    def __init__(self, manager, *args, **kwargs):
        super(AddSalary1View, self).__init__(*args, **kwargs)

        self._manager = manager

        self._init_ui()

    def _init_ui(self):
        employee_label = QLabel(self)
        employee_label.setText("Zaposleni*:")
        self.employee_box = QComboBox()
        for index, employee in enumerate(self._get_employees()):
            self.employee_box.insertItem(index, funcs.employee_unique_name(employee))
        employee_label.setBuddy(self.employee_box)

        net_label = QLabel(self)
        net_label.setText("Neto*:")
        self.net_line = QLineEdit(self)
        net_label.setBuddy(self.net_line)

        gross_label = QLabel(self)
        gross_label.setText("Bruto*:")
        self.gross_line = QLineEdit(self)
        gross_label.setBuddy(self.gross_line)

        date_label = QLabel(self)
        date_label.setText("Datum*:")
        self.calendar = QCalendarWidget(self)
        self.calendar.setFirstDayOfWeek(Qt.Monday)
        self.calendar.showToday()
        self.calendar.setGridVisible(True)
        date_label.setBuddy(self.calendar)

        add_button = QPushButton(self)
        add_button.setText("Dodaj")
        add_button.clicked.connect(self._add_salary)

        layout = QVBoxLayout()
        layout.addWidget(employee_label)
        layout.addWidget(self.employee_box)
        layout.addWidget(net_label)
        layout.addWidget(self.net_line)
        layout.addWidget(gross_label)
        layout.addWidget(self.gross_line)
        layout.addWidget(date_label)
        layout.addWidget(self.calendar)
        layout.addWidget(add_button)
        self.setLayout(layout)

    def _get_employees(self):
        return self._manager.actions(Actions.all_employees)

    def _add_salary(self):
        chosen_date = funcs.convert_date_to_string(self.calendar.selectedDate())
        values = [self.employee_box.currentText(), self.net_line.text(), self.gross_line.text(), chosen_date]

        response = self._manager.actions(Actions.add_salary_1, values)

        if response == Responses.success:
            QMessageBox.information(self, "Dodavanje plate 1", "Nova plata 1 je uspešno dodata!")
        elif response == Responses.fail:
            QMessageBox.warning(self, "Dodavanje plate 1", "Nova plata 1 nije uspešno dodata! Probajte opet.")
