from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from project.utils.enums import Actions, Responses
import project.utils.funcs as funcs


class AddSalary2View(QWidget):

    def __init__(self, manager, *args, **kwargs):
        super(AddSalary2View, self).__init__(*args, **kwargs)

        self._manager = manager

        self._init_ui()

    def _init_ui(self):
        employee_label = QLabel(self)
        employee_label.setText("Zaposleni*:")
        self.employee_box = QComboBox()
        for index, employee in enumerate(self._get_employees()):
            self.employee_box.insertItem(index, funcs.employee_unique_name(employee))
        employee_label.setBuddy(self.employee_box)

        day_label = QLabel(self)
        day_label.setText("Radnih dana:")
        self.day_line = QLineEdit(self)
        day_label.setBuddy(self.day_line)

        hour_label = QLabel(self)
        hour_label.setText("Radnih sati:")
        self.hour_line = QLineEdit(self)
        hour_label.setBuddy(self.hour_line)

        meal_label = QLabel(self)
        meal_label.setText("Obroka:")
        self.meal_line = QLineEdit(self)
        meal_label.setBuddy(self.meal_line)

        payment_label = QLabel(self)
        payment_label.setText("Rate:")
        self.payment_line = QLineEdit(self)
        payment_label.setBuddy(self.payment_line)

        vacation_label = QLabel(self)
        vacation_label.setText("Dana odmora:")
        self.vacation_line = QLineEdit(self)
        vacation_label.setBuddy(self.vacation_line)

        vacation_value_label = QLabel(self)
        vacation_value_label.setText("Odmor vrednost:")
        self.vacation_value_line = QLineEdit(self)
        vacation_value_label.setBuddy(self.vacation_value_line)

        fix_label = QLabel(self)
        fix_label.setText("Fiksno:")
        self.fix_line = QLineEdit(self)
        fix_label.setBuddy(self.fix_line)

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
        layout.addWidget(day_label)
        layout.addWidget(self.day_line)
        layout.addWidget(hour_label)
        layout.addWidget(self.hour_line)
        layout.addWidget(meal_label)
        layout.addWidget(self.meal_line)
        layout.addWidget(payment_label)
        layout.addWidget(self.payment_line)
        layout.addWidget(vacation_label)
        layout.addWidget(self.vacation_line)
        layout.addWidget(vacation_value_label)
        layout.addWidget(self.vacation_value_line)
        layout.addWidget(fix_label)
        layout.addWidget(self.fix_line)
        layout.addWidget(date_label)
        layout.addWidget(self.calendar)
        layout.addWidget(add_button)
        self.setLayout(layout)

    def _get_employees(self):
        return self._manager.actions(Actions.all_employees)

    def _add_salary(self):
        chosen_date = funcs.convert_date_to_string(self.calendar.selectedDate())
        values = [self.employee_box.currentText(), chosen_date, self.day_line.text(), None, self.hour_line.text(),
                  None, self.meal_line.text(), None, self.payment_line.text(), self.vacation_line.text(),
                  self.vacation_value_line.text(), self.fix_line.text()]

        response = self._manager.actions(Actions.add_salary_2, values)

        if response == Responses.success:
            QMessageBox.information(self, "Dodavanje plate 2", "Nova plata 2 je uspešno dodata!")
        elif response == Responses.fail:
            QMessageBox.warning(self, "Dodavanje plate 2", "Nova plata 2 nije uspešno dodata! Probajte opet.")
