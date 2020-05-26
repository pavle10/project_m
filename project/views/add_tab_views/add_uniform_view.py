from PyQt5.QtWidgets import *

from project.utils.enums import Actions, Responses
from project.utils import strings as strs


class AddUniformView(QWidget):

    def __init__(self, manager, *args, **kwargs):
        super(AddUniformView, self).__init__(*args, **kwargs)

        self._manager = manager

        self._init_ui()

    def _init_ui(self):
        name_label = QLabel(self)
        name_label.setText(f"*{strs.PRESENT_UNIFORM_HDR[0]}:")
        self.name_line = QLineEdit(self)
        name_label.setBuddy(self.name_line)

        add_button = QPushButton(self)
        add_button.setText(strs.ADD_BTN)
        add_button.clicked.connect(self._add_uniform)

        layout = QFormLayout()
        layout.addRow(name_label, self.name_line)
        layout.addWidget(add_button)
        self.setLayout(layout)

    def _add_uniform(self):
        response = self._manager.actions(Actions.add_uniform, [self.name_line.text()])

        if response == Responses.success:
            QMessageBox.information(self, strs.ADD_VIEW_MSG, strs.UNIFORM_ADD_SUCC_MSG)
        elif response == Responses.fail:
            QMessageBox.warning(self, strs.ADD_VIEW_MSG, strs.UNIFORM_ADD_FAIL_MSG)

