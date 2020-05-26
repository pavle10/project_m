import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from project.utils.enums import Actions, Responses
from project.utils import funcs as funcs, strings as strs, constants as cons


class AddUniformPieceView(QWidget):

    def __init__(self, manager, *args, **kwargs):
        super(AddUniformPieceView, self).__init__(*args, **kwargs)
        self._manager = manager

        self._init_ui()

    def _init_ui(self):
        uniform_label = QLabel(self)
        uniform_label.setText(f"*{strs.UNIFORM}:")
        self.uniform_box = QComboBox()
        for index, uniform in enumerate(self._get_uniforms()):
            self.uniform_box.insertItem(index, f"{uniform.get_name()}")
            uniform_label.setBuddy(self.uniform_box)

        employee_label = QLabel(self)
        employee_label.setText(f"*{strs.EMPLOYEE}:")
        self.employee_box = QComboBox()
        for index, employee in enumerate(self._get_employees()):
            self.employee_box.insertItem(index, funcs.employee_unique_name(employee))
        employee_label.setBuddy(self.employee_box)

        size_label = QLabel(self)
        size_label.setText(f"*{strs.PRESENT_UNIFORM_PIECE_HDR[1]}:")
        self.size_line = QLineEdit(self)
        size_label.setBuddy(self.size_line)

        quantity_label = QLabel(self)
        quantity_label.setText(f"*{strs.PRESENT_UNIFORM_PIECE_HDR[2]}:")
        self.quantity_line = QLineEdit(self)
        quantity_label.setBuddy(self.quantity_line)

        additional_label = QLabel(self)
        additional_label.setText(f"{strs.PRESENT_UNIFORM_PIECE_HDR[3]}:")
        self.additional_line = QLineEdit(self)
        additional_label.setBuddy(self.additional_line)

        date_label = QLabel(self)
        date_label.setText(f"*{strs.PRESENT_UNIFORM_PIECE_HDR[4]}:")
        self.date_line = QDateEdit(self)
        self.date_line.setDate(datetime.datetime.now().date())
        self.date_line.setDisplayFormat(cons.DATE_FORMAT_PYQT)
        date_label.setBuddy(self.date_line)

        add_button = QPushButton(self)
        add_button.setText(strs.ADD_BTN)
        add_button.clicked.connect(self._add_uniform_piece)

        layout = QFormLayout()
        layout.addRow(uniform_label, self.uniform_box)
        layout.addRow(employee_label, self.employee_box)
        layout.addRow(size_label, self.size_line)
        layout.addRow(quantity_label, self.quantity_line)
        layout.addRow(additional_label, self.additional_line)
        layout.addRow(date_label, self.date_line)
        layout.addWidget(add_button)
        self.setLayout(layout)

    def _get_uniforms(self):
        return self._manager.actions(Actions.all_uniforms)

    def _get_employees(self):
        return self._manager.actions(Actions.all_employees)

    def _add_uniform_piece(self):
        chosen_date = self.date_line.date().toPyDate()
        values = [self.uniform_box.currentText(), self.employee_box.currentText(), self.size_line.text(),
                  self.quantity_line.text(), self.additional_line.text(), chosen_date]

        response = self._manager.actions(Actions.add_uniform_piece, values)

        if response == Responses.success:
            QMessageBox.information(self, strs.ADD_VIEW_MSG, strs.UNIFORM_PIECE_ADD_SUCC_MSG)
        elif response == Responses.fail:
            QMessageBox.warning(self, strs.ADD_VIEW_MSG, strs.UNIFORM_PIECE_ADD_FAIL_MSG)
