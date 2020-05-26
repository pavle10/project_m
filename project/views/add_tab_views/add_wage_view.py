from PyQt5.QtWidgets import *

from project.utils.enums import Actions, Responses
from project.utils import funcs


class AddWageView(QWidget):

    def __init__(self, manager, *args, **kwargs):
        super(AddWageView, self).__init__(*args, **kwargs)

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
        day_label.setText("Dan*:")
        self.day_line = QLineEdit(self)
        day_label.setBuddy(self.day_line)

        hour_label = QLabel(self)
        hour_label.setText("Sat*:")
        self.hour_line = QLineEdit(self)
        hour_label.setBuddy(self.hour_line)

        meal_label = QLabel(self)
        meal_label.setText("Obrok*:")
        self.meal_line = QLineEdit(self)
        meal_label.setBuddy(self.meal_line)

        add_button = QPushButton(self)
        add_button.setText("Dodaj")
        add_button.clicked.connect(self._add_wage)

        layout = QVBoxLayout()
        layout.addWidget(employee_label)
        layout.addWidget(self.employee_box)
        layout.addWidget(day_label)
        layout.addWidget(self.day_line)
        layout.addWidget(hour_label)
        layout.addWidget(self.hour_line)
        layout.addWidget(meal_label)
        layout.addWidget(self.meal_line)
        layout.addWidget(add_button)
        self.setLayout(layout)

    def _get_employees(self):
        return self._manager.actions(Actions.all_employees)

    def _add_wage(self):
        values = [self.employee_box.currentText(), self.day_line.text(), self.hour_line.text(), self.meal_line.text()]

        response = self._manager.actions(Actions.add_wage, values)

        if response == Responses.success:
            QMessageBox.information(self, "Dodavanje dnevnice", "Nova dnevnica je uspešno dodata!")
        elif response == Responses.fail:
            QMessageBox.warning(self, "Dodavanje dnevnice", "Nova dnevnica nije uspešno dodata! Probajte opet.")


