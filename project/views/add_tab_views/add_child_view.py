from PyQt5.QtWidgets import *

from project.utils.enums import Actions, Responses
from project.utils import strings as strs, funcs


class AddChildView(QWidget):

    def __init__(self, manager, *args, **kwargs):
        super(AddChildView, self).__init__(*args, **kwargs)

        self._manager = manager

        self._init_ui()

    def _init_ui(self):
        identity_number_label = QLabel(self)
        identity_number_label.setText(f"{strs.PRESENT_CHILD_HDR[0]}:")
        self.identity_number_line = QLineEdit(self)
        identity_number_label.setBuddy(self.identity_number_line)

        birth_year_label = QLabel(self)
        birth_year_label.setText(f"*{strs.PRESENT_CHILD_HDR[1]}:")
        self.birth_year_line = QLineEdit(self)
        birth_year_label.setBuddy(self.birth_year_line)

        mother_label = QLabel(self)
        mother_label.setText(f"{strs.PRESENT_CHILD_HDR[2]}:")
        self.mother_box = QComboBox()
        self.mother_box.insertItem(0, strs.EMPTY)
        for index, employee in enumerate(self._get_employees()):
            self.mother_box.insertItem(index+1, funcs.employee_unique_name(employee))
        mother_label.setBuddy(self.mother_box)

        father_label = QLabel(self)
        father_label.setText(f"{strs.PRESENT_CHILD_HDR[3]}:")
        self.father_box = QComboBox()
        self.father_box.insertItem(0, strs.EMPTY)
        for index, employee in enumerate(self._get_employees()):
            self.father_box.insertItem(index+1, funcs.employee_unique_name(employee))
        father_label.setBuddy(self.father_box)

        add_button = QPushButton(self)
        add_button.setText(strs.ADD_BTN)
        add_button.clicked.connect(self._add_child)

        layout = QFormLayout()
        layout.addRow(identity_number_label, self.identity_number_line)
        layout.addRow(birth_year_label, self.birth_year_line)
        layout.addRow(mother_label, self.mother_box)
        layout.addRow(father_label, self.father_box)
        layout.addWidget(add_button)
        self.setLayout(layout)

    def _get_employees(self):
        return self._manager.actions(Actions.all_employees)

    def _add_child(self):
        mother = self.mother_box.currentText()
        father = self.father_box.currentText()

        if mother == strs.EMPTY and father == strs.EMPTY:
            QMessageBox.warning(self, strs.ADD_VIEW_MSG, strs.CHILD_ONE_PARENT_REQUIRED)

            return

        values = [self.identity_number_line.text(), self.birth_year_line.text(), mother, father]

        response = self._manager.actions(Actions.add_child, values)

        if response == Responses.success:
            QMessageBox.information(self, strs.ADD_VIEW_MSG, strs.CHILD_ADD_SUCC_MSG)
        elif response == Responses.fail:
            QMessageBox.warning(self, strs.ADD_VIEW_MSG, strs.CHILD_ADD_FAIL_MSG)

