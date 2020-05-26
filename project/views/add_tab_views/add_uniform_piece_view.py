from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from project.utils.enums import Actions, Responses
import project.utils.funcs as funcs


class AddUniformPieceView(QWidget):

    def __init__(self, manager, *args, **kwargs):
        super(AddUniformPieceView, self).__init__(*args, **kwargs)
        self._manager = manager

        self._init_ui()

    def _init_ui(self):
        uniform_label = QLabel(self)
        uniform_label.setText("Radno odelo:")
        self.uniform_box = QComboBox()
        for index, uniform in enumerate(self._get_uniforms()):
            self.uniform_box.insertItem(index, f"{uniform.get_name()}")
            uniform_label.setBuddy(self.uniform_box)

        employee_label = QLabel(self)
        employee_label.setText("Zaposleni:")
        self.employee_box = QComboBox()
        for index, employee in enumerate(self._get_employees()):
            self.employee_box.insertItem(index, funcs.employee_unique_name(employee))
        employee_label.setBuddy(self.employee_box)

        size_label = QLabel(self)
        size_label.setText("Veličina:")
        self.size_line = QLineEdit(self)
        size_label.setBuddy(self.size_line)

        quantity_label = QLabel(self)
        quantity_label.setText("Količina:")
        self.quantity_line = QLineEdit(self)
        quantity_label.setBuddy(self.quantity_line)

        additional_label = QLabel(self)
        additional_label.setText("Dodatno:")
        self.additional_line = QLineEdit(self)
        additional_label.setBuddy(self.additional_line)

        date_label = QLabel(self)
        date_label.setText("Datum:")
        self.calendar = QCalendarWidget(self)
        self.calendar.setFirstDayOfWeek(Qt.Monday)
        self.calendar.showToday()
        self.calendar.setGridVisible(True)
        date_label.setBuddy(self.calendar)

        add_button = QPushButton(self)
        add_button.setText("Dodaj")
        add_button.clicked.connect(self._add_uniform_piece)

        layout = QVBoxLayout()
        layout.addWidget(uniform_label)
        layout.addWidget(self.uniform_box)
        layout.addWidget(employee_label)
        layout.addWidget(self.employee_box)
        layout.addWidget(size_label)
        layout.addWidget(self.size_line)
        layout.addWidget(quantity_label)
        layout.addWidget(self.quantity_line)
        layout.addWidget(additional_label)
        layout.addWidget(self.additional_line)
        layout.addWidget(date_label)
        layout.addWidget(self.calendar)
        layout.addWidget(add_button)
        self.setLayout(layout)

    def _get_uniforms(self):
        return self._manager.actions(Actions.all_uniforms)

    def _get_employees(self):
        return self._manager.actions(Actions.all_employees)

    def _add_uniform_piece(self):
        chosen_date = funcs.convert_date_to_string(self.calendar.selectedDate())
        values = [self.uniform_box.currentText(), self.employee_box.currentText(), self.size_line.text(),
                  self.quantity_line.text(), self.additional_line.text(), chosen_date]

        response = self._manager.actions(Actions.add_uniform_piece, values)

        if response == Responses.success:
            QMessageBox.information(self, "Popis odela", "Nova jedinica je uspešno dodata!")
        elif response == Responses.fail:
            QMessageBox.warning(self, "Popis odela", "Nova jedinica nije uspešno dodata! Probajte opet.")
