from PyQt5.QtWidgets import *

from project.enums.actions import Actions
from project.enums.responses import Responses


class AddChildView(QWidget):

    def __init__(self, manager, *args, **kwargs):
        super(AddChildView, self).__init__(*args, **kwargs)

        self._manager = manager

        self._init_ui()

    def _init_ui(self):
        identity_number_label = QLabel(self)
        identity_number_label.setText("JMBG:")
        self.identity_number_line = QLineEdit(self)
        identity_number_label.setBuddy(self.identity_number_line)

        birth_year_label = QLabel(self)
        birth_year_label.setText("Godina rodjenja:")
        self.birth_year_line = QLineEdit(self)
        birth_year_label.setBuddy(self.birth_year_line)

        mother_label = QLabel(self)
        mother_label.setText("Majka:")
        self.mother_box = QComboBox()
        self.mother_box.insertItem(0, "Prazno")
        for index, employee in enumerate(self._get_employees()):
            self.mother_box.insertItem(index+1, f"{employee[0]} {employee[1]} {employee[2]}")
        mother_label.setBuddy(self.mother_box)

        father_label = QLabel(self)
        father_label.setText("Otac:")
        self.father_box = QComboBox()
        self.father_box.insertItem(0, "Prazno")
        for index, employee in enumerate(self._get_employees()):
            self.father_box.insertItem(index+1, f"{employee[0]} {employee[1]} {employee[2]}")
        father_label.setBuddy(self.father_box)

        add_button = QPushButton(self)
        add_button.setText("Dodaj")
        add_button.clicked.connect(self._add_child)

        layout = QVBoxLayout()
        layout.addWidget(identity_number_label)
        layout.addWidget(self.identity_number_line)
        layout.addWidget(birth_year_label)
        layout.addWidget(self.birth_year_line)
        layout.addWidget(mother_label)
        layout.addWidget(self.mother_box)
        layout.addWidget(father_label)
        layout.addWidget(self.father_box)
        layout.addWidget(add_button)
        self.setLayout(layout)

    def _get_employees(self):
        return self._manager.actions(Actions.all_employees)

    def _add_child(self):
        mother = self.mother_box.currentText()
        father = self.father_box.currentText()

        if mother == "Prazno" and father == "Prazno":
            QMessageBox.warning(self, "Dodavanje deteta", "Bar jedan roditelj mora biti izabran!")

            return

        values = [self.identity_number_line.text(), self.birth_year_line.text(), mother, father]

        response = self._manager.actions(Actions.add_child, values)

        if response == Responses.success:
            QMessageBox.information(self, "Dodavanje deteta", "Novo dete je uspešno dodato!")
        elif response == Responses.fail:
            QMessageBox.warning(self, "Dodavanje deteta", "Novo dete nije uspešno dodato! Probajte opet.")

