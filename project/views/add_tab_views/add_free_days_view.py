from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from project.utils.enums import Actions, Responses
import project.utils.funcs as funcs


class AddFreeDaysView(QWidget):

    def __init__(self, manager, *args, **kwargs):
        super(AddFreeDaysView, self).__init__(*args, **kwargs)

        self._manager = manager

        self._init_ui()

    def _init_ui(self):
        employee_label = QLabel(self)
        employee_label.setText("Zaposleni:")
        self.employee_box = QComboBox()
        for index, employee in enumerate(self._get_employees()):
            self.employee_box.insertItem(index, funcs.employee_unique_name(employee))
        employee_label.setBuddy(self.employee_box)

        reason_label = QLabel(self)
        reason_label.setText("Razlog:")
        self.reason_line = QLineEdit(self)
        reason_label.setBuddy(self.reason_line)

        start_date_label = QLabel(self)
        start_date_label.setText("Datum:")
        self.start_calendar = QCalendarWidget(self)
        self.start_calendar.setFirstDayOfWeek(Qt.Monday)
        self.start_calendar.showToday()
        self.start_calendar.setGridVisible(True)
        start_date_label.setBuddy(self.start_calendar)

        end_date_label = QLabel(self)
        end_date_label.setText("Datum:")
        self.end_calendar = QCalendarWidget(self)
        self.end_calendar.setFirstDayOfWeek(Qt.Monday)
        self.end_calendar.showToday()
        self.end_calendar.setGridVisible(True)
        end_date_label.setBuddy(self.end_calendar)

        add_button = QPushButton(self)
        add_button.setText("Dodaj")
        add_button.clicked.connect(self._add_free_days)

        layout = QVBoxLayout()
        layout.addWidget(employee_label)
        layout.addWidget(self.employee_box)
        layout.addWidget(reason_label)
        layout.addWidget(self.reason_line)
        layout.addWidget(start_date_label)
        layout.addWidget(self.start_calendar)
        layout.addWidget(end_date_label)
        layout.addWidget(self.end_calendar)
        layout.addWidget(add_button)
        self.setLayout(layout)

    def _get_employees(self):
        return self._manager.actions(Actions.all_employees)

    def _add_free_days(self):
        start_date = funcs.convert_date_to_string(self.start_calendar.selectedDate())
        end_date = funcs.convert_date_to_string(self.end_calendar.selectedDate())
        total_days = self.end_calendar.selectedDate().toPyDate() - self.start_calendar.selectedDate().toPyDate()

        values = [self.employee_box.currentText(), start_date, end_date, total_days.days,  self.reason_line.text()]

        response = self._manager.actions(Actions.add_free_days, values)

        if response == Responses.success:
            QMessageBox.information(self, "Dodavanje slobodnih dana", "Slobodni dani su uspešno dodati!")
        elif response == Responses.fail:
            QMessageBox.warning(self, "Dodavanje slobodnih dana", "Slobodni dani nisu uspešno dodati! Probajte opet.")
