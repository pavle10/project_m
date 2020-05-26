from PyQt5.QtWidgets import *

from project.utils.enums import Actions, Responses
from project.utils import strings as strs


class AddPositionView(QWidget):

    def __init__(self, manager, *args, **kwargs):
        super(AddPositionView, self).__init__(*args, **kwargs)
        self._manager = manager

        self._init_ui()

    def _init_ui(self):
        name_label = QLabel(self)
        name_label.setText(f"*{strs.PRESENT_POSITION_HDR[0]}:")
        self.name_line = QLineEdit(self)
        name_label.setBuddy(self.name_line)

        saturday_label = QLabel(self)
        saturday_label.setText(f"*{strs.PRESENT_POSITION_HDR[1]}:")
        self.saturday = QComboBox()
        self.saturday.addItem(strs.YES)
        self.saturday.addItem(strs.NO)
        saturday_label.setBuddy(self.saturday)

        add_button = QPushButton(self)
        add_button.setText(strs.ADD_BTN)
        add_button.clicked.connect(self._add_position)

        layout = QFormLayout()
        layout.addRow(name_label, self.name_line)
        layout.addRow(saturday_label, self.saturday)
        layout.addWidget(add_button)
        self.setLayout(layout)

    def _add_position(self):
        response = self._manager.actions(Actions.add_position, [self.name_line.text(), self.saturday.currentText()])

        if response == Responses.success:
            QMessageBox.information(self, strs.ADD_VIEW_MSG, strs.POSITION_ADD_SUCC_MSG)
        elif response == Responses.fail:
            QMessageBox.warning(self, strs.ADD_VIEW_MSG, strs.POSITION_ADD_FAIL_MSG)
