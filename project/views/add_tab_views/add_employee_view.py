import datetime
from PyQt5.QtWidgets import *

from project.utils.enums import Actions, Responses
from project.utils import constants as cons, strings as strs


class AddEmployeeView(QWidget):

    def __init__(self, manager, *args, **kwargs):
        super(AddEmployeeView, self).__init__(*args, **kwargs)
        self._manager = manager

        self._init_ui()

    def _init_ui(self):
        first_name_label = QLabel(self)
        first_name_label.setText(f"*{strs.PRESENT_EMPLOYEE_HDR[0]}:")
        self.first_name_line = QLineEdit(self)
        first_name_label.setBuddy(self.first_name_line)

        last_name_label = QLabel(self)
        last_name_label.setText(f"*{strs.PRESENT_EMPLOYEE_HDR[1]}:")
        self.last_name_line = QLineEdit(self)
        last_name_label.setBuddy(self.last_name_line)

        fathers_name_label = QLabel(self)
        fathers_name_label.setText(f"{strs.PRESENT_EMPLOYEE_HDR[2]}:")
        self.fathers_name_line = QLineEdit(self)
        fathers_name_label.setBuddy(self.fathers_name_line)

        identity_number_label = QLabel(self)
        identity_number_label.setText(f"*{strs.PRESENT_EMPLOYEE_HDR[3]}:")
        self.identity_number_line = QLineEdit(self)
        identity_number_label.setBuddy(self.identity_number_line)

        personal_card_label = QLabel(self)
        personal_card_label.setText(f"{strs.PRESENT_EMPLOYEE_HDR[4]}:")
        self.personal_card_line = QLineEdit(self)
        personal_card_label.setBuddy(self.personal_card_line)

        qualification_label = QLabel(self)
        qualification_label.setText(f"{strs.PRESENT_EMPLOYEE_HDR[5]}:")
        self.qualification_line = QLineEdit(self)
        qualification_label.setBuddy(self.qualification_line)

        position_label = QLabel(self)
        position_label.setText(f"{strs.PRESENT_EMPLOYEE_HDR[6]}:")
        self.position_box = QComboBox()
        for index, position in enumerate(self._get_positions()):
            self.position_box.insertItem(index, position.get_name())
        position_label.setBuddy(self.position_box)

        saint_day_label = QLabel(self)
        saint_day_label.setText(f"{strs.PRESENT_EMPLOYEE_HDR[7]}:")
        self.saint_day_line = QLineEdit(self)
        saint_day_label.setBuddy(self.saint_day_line)

        address_label = QLabel(self)
        address_label.setText(f"*{strs.PRESENT_EMPLOYEE_HDR[8]}:")
        self.address_line = QLineEdit(self)
        address_label.setBuddy(self.address_line)

        account_label = QLabel(self)
        account_label.setText(f"{strs.PRESENT_EMPLOYEE_HDR[9]}:")
        self.account_line = QLineEdit(self)
        account_label.setBuddy(self.account_line)

        before_m_label = QLabel(self)
        before_m_label.setText(f"{strs.PRESENT_EMPLOYEE_HDR[10]}:")
        self.before_m_line = QLineEdit(self)
        before_m_label.setBuddy(self.before_m_line)

        start_date_label = QLabel(self)
        start_date_label.setText(f"{strs.PRESENT_EMPLOYEE_HDR[11]}:")
        self.start_date_line = QDateEdit(self)
        self.start_date_line.setDate(datetime.datetime.now().date())
        self.start_date_line.setDisplayFormat(cons.DATE_FORMAT_PYQT)
        start_date_label.setBuddy(self.start_date_line)

        home_number_label = QLabel(self)
        home_number_label.setText(f"{strs.PRESENT_EMPLOYEE_HDR[12]}:")
        self.home_number_line = QLineEdit(self)
        home_number_label.setBuddy(self.home_number_line)

        mobile_number_label = QLabel(self)
        mobile_number_label.setText(f"{strs.PRESENT_EMPLOYEE_HDR[13]}:")
        self.mobile_number_line = QLineEdit(self)
        mobile_number_label.setBuddy(self.mobile_number_line)

        situation_label = QLabel(self)
        situation_label.setText(f"{strs.PRESENT_EMPLOYEE_HDR[14]}:")
        self.situation_line = QLineEdit(self)
        situation_label.setBuddy(self.situation_line)

        add_button = QPushButton(self)
        add_button.setText(strs.ADD_BTN)
        add_button.clicked.connect(self._add_employee)

        layout = QFormLayout()
        layout.addRow(first_name_label, self.first_name_line)
        layout.addRow(last_name_label, self.last_name_line)
        layout.addRow(fathers_name_label, self.fathers_name_line)
        layout.addRow(identity_number_label, self.identity_number_line)
        layout.addRow(personal_card_label, self.personal_card_line)
        layout.addRow(qualification_label, self.qualification_line)
        layout.addRow(position_label, self.position_box)
        layout.addRow(saint_day_label, self.saint_day_line)
        layout.addRow(address_label, self.address_line)
        layout.addRow(account_label, self.account_line)
        layout.addRow(before_m_label, self.before_m_line)
        layout.addRow(start_date_label, self.start_date_line)
        layout.addRow(home_number_label, self.home_number_line)
        layout.addRow(mobile_number_label, self.mobile_number_line)
        layout.addRow(situation_label, self.situation_line)
        layout.addWidget(add_button)
        self.setLayout(layout)

    def _add_employee(self):
        values = [self.first_name_line.text(), self.last_name_line.text(), self.fathers_name_line.text(),
                  self.identity_number_line.text(), self.personal_card_line.text(), self.qualification_line.text(),
                  self.position_box.currentText(), self.saint_day_line.text(), self.address_line.text(),
                  self.account_line.text(), self.before_m_line.text(), self.start_date_line.text(),
                  self.home_number_line.text(), self.mobile_number_line.text(), self.situation_line.text()]
        response = self._manager.actions(Actions.add_employee, values)

        if response == Responses.success:
            QMessageBox.information(self, strs.ADD_VIEW_MSG, strs.EMPLOYEE_ADD_SUCC_MSG)
        elif response == Responses.fail:
            QMessageBox.warning(self, strs.ADD_VIEW_MSG, strs.EMPLOYEE_ADD_FAIL_MSG)

    def _get_positions(self):
        return self._manager.actions(Actions.all_positions)
