from PyQt5.QtWidgets import *


class AddEmployeeView(QWidget):

    def __init__(self, manager, *args, **kwargs):
        super(AddEmployeeView, self).__init__(*args, **kwargs)
        self._manager = manager

        self._init_ui()

    def _init_ui(self):
        label = QLabel(self)
        label.setText("Dodavanje zaposlenog")

        layout = QVBoxLayout()
        layout.addWidget(label)

        self.setLayout(layout)
