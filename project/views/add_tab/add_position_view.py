from PyQt5.QtWidgets import *

from project.utils.enums import Actions, Responses


class AddPositionView(QWidget):

    def __init__(self, manager, *args, **kwargs):
        super(AddPositionView, self).__init__(*args, **kwargs)
        self._manager = manager

        self._init_ui()

    def _init_ui(self):
        name_label = QLabel(self)
        name_label.setText("Naziv:")

        self.name_line = QLineEdit(self)
        name_label.setBuddy(self.name_line)

        saturday_label = QLabel(self)
        saturday_label.setText("Radna subota")

        self.saturday = QComboBox()
        self.saturday.addItem("Da")
        self.saturday.addItem("Ne")
        saturday_label.setBuddy(self.saturday)

        add_button = QPushButton(self)
        add_button.setText("Dodaj")
        add_button.clicked.connect(self._add_position)

        layout = QVBoxLayout()
        layout.addWidget(name_label)
        layout.addWidget(self.name_line)
        layout.addWidget(saturday_label)
        layout.addWidget(self.saturday)
        layout.addWidget(add_button)
        self.setLayout(layout)

    def _add_position(self):
        response = self._manager.actions(Actions.add_position, [self.name_line.text(), self.saturday.currentText()])

        if response == Responses.success:
            QMessageBox.information(self, "Dodavanje pozicije", "Nova pozicija je uspešno dodata!")
        elif response == Responses.fail:
            QMessageBox.warning(self, "Dodavanje pozicije", "Nova pozicija nije uspešno dodata! Probajte opet.")



