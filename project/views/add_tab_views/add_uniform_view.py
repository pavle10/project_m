from PyQt5.QtWidgets import *

from project.utils.enums import Actions, Responses


class AddUniformView(QWidget):

    def __init__(self, manager, *args, **kwargs):
        super(AddUniformView, self).__init__(*args, **kwargs)

        self._manager = manager

        self._init_ui()

    def _init_ui(self):
        name_label = QLabel(self)
        name_label.setText("Naziv:")

        self.name_line = QLineEdit(self)
        name_label.setBuddy(self.name_line)

        add_button = QPushButton(self)
        add_button.setText("Dodaj")
        add_button.clicked.connect(self._add_uniform)

        layout = QVBoxLayout()
        layout.addWidget(name_label)
        layout.addWidget(self.name_line)
        layout.addWidget(add_button)
        self.setLayout(layout)

    def _add_uniform(self):
        response = self._manager.actions(Actions.add_uniform, [self.name_line.text()])

        if response == Responses.success:
            QMessageBox.information(self, "Dodavanje odela", "Novo odelo je uspešno dodato!")
        elif response == Responses.fail:
            QMessageBox.warning(self, "Dodavanje odela", "Novo odelo nije uspešno dodato! Probajte opet.")

