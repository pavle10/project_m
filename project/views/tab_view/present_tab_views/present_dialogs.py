from PyQt5.QtWidgets import *

from project.utils import constants as cons, strings as strs, funcs
from project.models.my_widgets import *


class DeleteRowDialog(QDialog):

    def __init__(self, *args, **kwargs):
        super(DeleteRowDialog, self).__init__(*args, **kwargs)

        self.setWindowTitle(strs.PRESENT_VIEW_MSG)
        self.resize(cons.DIALOGS_WIDTH, cons.DIALOGS_HEIGHT)

        question_label = QLabel(self)
        question_label.setText(strs.DELETE_DIALOG_MSG)

        button_box = QDialogButtonBox(QDialogButtonBox.Yes | QDialogButtonBox.No)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        layout = QVBoxLayout()
        layout.addWidget(question_label)
        layout.addWidget(button_box)
        self.setLayout(layout)


class UpdateEmployeeDialog(QDialog):

    def __init__(self, selected_data, positions, *args, **kwargs):
        super(UpdateEmployeeDialog, self).__init__(*args, **kwargs)
        self.data = selected_data

        self.setWindowTitle(strs.PRESENT_VIEW_MSG)

        first_name_label = MyLabel(strs.PRESENT_EMPLOYEE_HDR[0])
        self.first_name_line = MyEditLine(selected_data[1])
        first_name_label.setBuddy(self.first_name_line)

        last_name_label = MyLabel(strs.PRESENT_EMPLOYEE_HDR[1])
        self.last_name_line = MyEditLine(selected_data[2])
        last_name_label.setBuddy(self.last_name_line)

        fathers_name_label = MyLabel(strs.PRESENT_EMPLOYEE_HDR[2])
        self.fathers_name_line = MyEditLine(selected_data[3])
        fathers_name_label.setBuddy(self.fathers_name_line)

        identity_number_label = MyLabel(strs.PRESENT_EMPLOYEE_HDR[3])
        self.identity_number_line = MyEditLine(selected_data[4])
        identity_number_label.setBuddy(self.identity_number_line)

        personal_card_label = MyLabel(strs.PRESENT_EMPLOYEE_HDR[4])
        self.personal_card_line = MyEditLine(selected_data[5])
        personal_card_label.setBuddy(self.personal_card_line)

        qualification_label = MyLabel(strs.PRESENT_EMPLOYEE_HDR[5])
        self.qualification_line = MyEditLine(selected_data[6])
        qualification_label.setBuddy(self.qualification_line)

        position_label = MyLabel(strs.PRESENT_EMPLOYEE_HDR[6])
        self.position_box = MyComboBox()
        current_index = 0
        for index, position in enumerate(positions):
            self.position_box.insertItem(index, position.get_name())
            current_index = index if position.get_position_id() == selected_data[7] else 0
        self.position_box.setCurrentIndex(current_index)
        position_label.setBuddy(self.position_box)

        saint_day_label = MyLabel(strs.PRESENT_EMPLOYEE_HDR[7])
        self.saint_day_line = MyEditLine(selected_data[8])
        saint_day_label.setBuddy(self.saint_day_line)

        address_label = MyLabel(strs.PRESENT_EMPLOYEE_HDR[8])
        self.address_line = MyEditLine(selected_data[9])
        address_label.setBuddy(self.address_line)

        account_label = MyLabel(strs.PRESENT_EMPLOYEE_HDR[9])
        self.account_line = MyEditLine(selected_data[10])
        account_label.setBuddy(self.account_line)

        before_m_label = MyLabel(strs.PRESENT_EMPLOYEE_HDR[10])
        years_label = MyLabelShort(strs.YEARS)
        self.years_line = MyEditLineShort()
        months_label = MyLabelShort(strs.MONTHS)
        self.months_line = MyEditLineShort()
        days_label = MyLabelShort(strs.DAYS)
        self.days_line = MyEditLineShort()
        before_layout = QHBoxLayout()
        before_layout.addWidget(years_label)
        before_layout.addWidget(self.years_line)
        before_layout.addWidget(months_label)
        before_layout.addWidget(self.months_line)
        before_layout.addWidget(days_label)
        before_layout.addWidget(self.days_line)

        start_date_label = MyLabel(strs.PRESENT_EMPLOYEE_HDR[11])
        self.start_date_line = MyEditDate(selected_data[12])
        start_date_label.setBuddy(self.start_date_line)

        home_number_label = MyLabel(strs.PRESENT_EMPLOYEE_HDR[12])
        self.home_number_line = MyEditLine(selected_data[13])
        home_number_label.setBuddy(self.home_number_line)

        mobile_number_label = MyLabel(strs.PRESENT_EMPLOYEE_HDR[13])
        self.mobile_number_line = MyEditLine(selected_data[14])
        mobile_number_label.setBuddy(self.mobile_number_line)

        situation_label = MyLabel(strs.PRESENT_EMPLOYEE_HDR[14])
        self.situation_line = MyEditLine(selected_data[15])
        situation_label.setBuddy(self.situation_line)

        button_box = QDialogButtonBox(QDialogButtonBox.Yes | QDialogButtonBox.No)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

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
        layout.addRow(before_m_label, before_layout)
        layout.addRow(start_date_label, self.start_date_line)
        layout.addRow(home_number_label, self.home_number_line)
        layout.addRow(mobile_number_label, self.mobile_number_line)
        layout.addRow(situation_label, self.situation_line)
        layout.addWidget(button_box)
        self.setLayout(layout)

    def get_value(self):
        self.data[1] = self.first_name_line.text()
        self.data[2] = self.last_name_line.text()
        self.data[3] = self.fathers_name_line.text()
        self.data[4] = self.identity_number_line.text()
        self.data[5] = self.personal_card_line.text()
        self.data[6] = self.qualification_line.text()
        self.data[7] = self.position_box.currentText()
        self.data[8] = self.saint_day_line.text()
        self.data[9] = self.address_line.text()
        self.data[10] = self.account_line.text()
        self.data[11] = [self.years_line.text(), self.months_line.text(), self.days_line.text()]
        self.data[12] = self.start_date_line.date().toPyDate()
        self.data[13] = self.home_number_line.text()
        self.data[14] = self.mobile_number_line.text()
        self.data[15] = self.situation_line.text()

        return self.data


class UpdatePositionDialog(QDialog):

    def __init__(self, selected_data, *args, **kwargs):
        super(UpdatePositionDialog, self).__init__(*args, **kwargs)
        self.data = selected_data

        self.setWindowTitle(strs.PRESENT_VIEW_MSG)

        name_label = MyLabel(strs.PRESENT_CHILD_HDR[0])
        self.name_line = MyEditLine(selected_data[1])
        name_label.setBuddy(self.name_line)

        saturday_label = MyLabel(strs.PRESENT_POSITION_HDR[1])
        self.saturday = MyComboBox()
        self.saturday.addItem(strs.YES)
        self.saturday.addItem(strs.NO)
        self.saturday.setCurrentIndex(selected_data[2])
        saturday_label.setBuddy(self.saturday)

        button_box = QDialogButtonBox(QDialogButtonBox.Yes | QDialogButtonBox.No)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        layout = QFormLayout()
        layout.addRow(name_label, self.name_line)
        layout.addRow(saturday_label, self.saturday)
        layout.addRow(button_box)
        self.setLayout(layout)

    def get_value(self):
        self.data[1] = self.name_line.text()
        self.data[2] = funcs.convert_saturday(self.saturday.currentText())

        return self.data


class UpdateChildDialog(QDialog):

    def __init__(self, selected_data, employees, *args, **kwargs):
        super(UpdateChildDialog, self).__init__(*args, **kwargs)
        self.data = selected_data

        self.setWindowTitle(strs.PRESENT_VIEW_MSG)

        first_name_label = MyLabel(strs.PRESENT_CHILD_HDR[0])
        self.first_name_line = MyEditLine(selected_data[1])
        first_name_label.setBuddy(self.first_name_line)

        last_name_label = MyLabel(strs.PRESENT_CHILD_HDR[1])
        self.last_name_line = MyEditLine(selected_data[2])
        last_name_label.setBuddy(self.last_name_line)

        identity_number_label = MyLabel(strs.PRESENT_CHILD_HDR[2])
        self.identity_number_line = MyEditLine(selected_data[3])
        identity_number_label.setBuddy(self.identity_number_line)

        birthday_label = MyLabel(strs.PRESENT_CHILD_HDR[3])
        self.birthday_line = MyEditLine(selected_data[4])
        birthday_label.setBuddy(self.birthday_line)

        mother_label = MyLabel(strs.PRESENT_CHILD_HDR[3])
        self.mother_box = MyComboBox()
        self.mother_box.insertItem(0, "")
        select_index = 0
        for index, employee in enumerate(employees):
            self.mother_box.insertItem(index + 1, funcs.employee_unique_name(employee))
            select_index = index + 1 if employee.get_employee_id() == selected_data[3] else select_index
        self.mother_box.setCurrentIndex(select_index)
        mother_label.setBuddy(self.mother_box)

        father_label = MyLabel(strs.PRESENT_CHILD_HDR[4])
        self.father_box = MyComboBox()
        self.father_box.insertItem(0, "")
        select_index = 0
        for index, employee in enumerate(employees):
            self.father_box.insertItem(index + 1, funcs.employee_unique_name(employee))
            select_index = index + 1 if employee.get_employee_id() == selected_data[5] else select_index
        self.father_box.setCurrentIndex(select_index)
        father_label.setBuddy(self.father_box)

        button_box = QDialogButtonBox(QDialogButtonBox.Yes | QDialogButtonBox.No)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        layout = QFormLayout()
        layout.addRow(first_name_label, self.first_name_line)
        layout.addRow(last_name_label, self.last_name_line)
        layout.addRow(identity_number_label, self.identity_number_line)
        layout.addRow(birthday_label, self.birthday_line)
        layout.addRow(mother_label, self.mother_box)
        layout.addRow(father_label, self.father_box)
        layout.addRow(button_box)
        self.setLayout(layout)

    def get_value(self):
        self.data[1] = self.first_name_line.text()
        self.data[2] = self.last_name_line.text()
        self.data[3] = self.identity_number_line.text()
        self.data[4] = self.birthday_line.text()
        self.data[6] = self.mother_box.currentText()
        self.data[8] = self.father_box.currentText()

        return self.data


class UpdateUniformDialog(QDialog):

    def __init__(self, selected_data, *args, **kwargs):
        super(UpdateUniformDialog, self).__init__(*args, **kwargs)
        self.data = selected_data

        self.setWindowTitle(strs.PRESENT_VIEW_MSG)

        name_label = MyLabel(strs.PRESENT_UNIFORM_HDR[0])
        self.name_line = MyEditLine(selected_data[0])
        name_label.setBuddy(self.name_line)

        button_box = QDialogButtonBox(QDialogButtonBox.Yes | QDialogButtonBox.No)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        layout = QFormLayout()
        layout.addRow(name_label, self.name_line)
        layout.addRow(button_box)
        self.setLayout(layout)

    def get_value(self):
        self.data[1] = self.name_line.text()

        return self.data


class UpdateUniformPieceDialog(QDialog):

    def __init__(self, selected_data, uniforms, *args, **kwargs):
        super(UpdateUniformPieceDialog, self).__init__(*args, **kwargs)
        self.data = selected_data
        self.uniforms = uniforms

        self.setWindowTitle(strs.PRESENT_VIEW_MSG)

        uniform_label = MyLabel(strs.PRESENT_UNIFORM_PIECE_HDR[0])
        self.uniform_box = MyComboBox()
        current_index = 0
        for index, uniform in enumerate(self.uniforms):
            self.uniform_box.insertItem(index, uniform.get_name())
            if uniform.get_uniform_id() == selected_data[1]:
                current_index = index
        self.uniform_box.setCurrentIndex(current_index)
        uniform_label.setBuddy(self.uniform_box)

        size_label = MyLabel(strs.PRESENT_UNIFORM_PIECE_HDR[1])
        self.size_line = MyEditLine(str(selected_data[3]))
        size_label.setBuddy(self.size_line)

        quantity_label = MyLabel(strs.PRESENT_UNIFORM_PIECE_HDR[2])
        self.quantity_line = MyEditLine(str(selected_data[4]))
        quantity_label.setBuddy(self.quantity_line)

        additional_label = MyLabel(strs.PRESENT_UNIFORM_PIECE_HDR[3])
        self.additional_line = MyEditLine(selected_data[5])
        additional_label.setBuddy(self.additional_line)

        date_label = MyLabel(strs.PRESENT_UNIFORM_PIECE_HDR[4])
        self.date_line = MyEditDate(selected_data[6])
        date_label.setBuddy(self.date_line)

        button_box = QDialogButtonBox(QDialogButtonBox.Yes | QDialogButtonBox.No)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        layout = QFormLayout()
        layout.addRow(uniform_label, self.uniform_box)
        layout.addRow(size_label, self.size_line)
        layout.addRow(quantity_label, self.quantity_line)
        layout.addRow(additional_label, self.additional_line)
        layout.addRow(date_label, self.date_line)
        layout.addRow(button_box)
        self.setLayout(layout)

    def get_value(self):
        uniform = self.uniforms[self.uniform_box.currentIndex()]

        self.data[1] = uniform.get_uniform_id()
        self.data[3] = self.size_line.text()
        self.data[4] = self.quantity_line.text()
        self.data[5] = self.additional_line.text()
        self.data[6] = self.date_line.date().toPyDate()

        return self.data


class UpdateFreeDaysRowDialog(QDialog):

    def __init__(self, selected_data, *args, **kwargs):
        super(UpdateFreeDaysRowDialog, self).__init__(*args, **kwargs)
        self.data = selected_data

        self.setWindowTitle(strs.PRESENT_VIEW_MSG)

        start_date_label = MyLabel(strs.PRESENT_FREE_DAYS_HDR[0])
        self.start_date_line = MyEditDate(selected_data[2])
        start_date_label.setBuddy(self.start_date_line)

        end_date_label = MyLabel(strs.PRESENT_FREE_DAYS_HDR[1])
        self.end_date_line = MyEditDate(selected_data[3])
        end_date_label.setBuddy(self.end_date_line)

        reason_label = MyLabel(strs.PRESENT_FREE_DAYS_HDR[3])
        self.reason_line = MyEditLine(selected_data[5])
        reason_label.setBuddy(self.reason_line)

        button_box = QDialogButtonBox(QDialogButtonBox.Yes | QDialogButtonBox.No)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        layout = QFormLayout()
        layout.addRow(start_date_label, self.start_date_line)
        layout.addRow(end_date_label, self.end_date_line)
        layout.addRow(reason_label, self.reason_line)
        layout.addRow(button_box)
        self.setLayout(layout)

    def get_value(self):
        self.data[2] = self.start_date_line.date().toPyDate()
        self.data[3] = self.end_date_line.date().toPyDate()
        self.data[4] = funcs.count_free_days(self.data[2], self.data[3])
        self.data[5] = self.reason_line.text()

        return self.data


class UpdateWageRowDialog(QDialog):

    def __init__(self, selected_data, *args, **kwargs):
        super(UpdateWageRowDialog, self).__init__(*args, **kwargs)
        self.data = selected_data

        self.setWindowTitle(strs.PRESENT_VIEW_MSG)

        day_label = MyLabel(strs.PRESENT_WAGE_HDR[0])
        self.day_line = MyEditLine(str(selected_data[2]))
        day_label.setBuddy(self.day_line)

        hour_label = MyLabel(strs.PRESENT_WAGE_HDR[1])
        self.hour_line = MyEditLine(str(selected_data[3]))
        hour_label.setBuddy(self.hour_line)

        meal_label = MyLabel(strs.PRESENT_WAGE_HDR[2])
        self.meal_line = MyEditLine(str(selected_data[4]))
        meal_label.setBuddy(self.meal_line)

        button_box = QDialogButtonBox(QDialogButtonBox.Yes | QDialogButtonBox.No)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        layout = QFormLayout()
        layout.addRow(day_label, self.day_line)
        layout.addRow(hour_label, self.hour_line)
        layout.addRow(meal_label, self.meal_line)
        layout.addRow(button_box)
        self.setLayout(layout)

    def get_value(self):
        self.data[2] = self.day_line.text()
        self.data[3] = self.hour_line.text()
        self.data[4] = self.meal_line.text()

        return self.data


class UpdateSalary1RowDialog(QDialog):

    def __init__(self, selected_data, *args, **kwargs):
        super(UpdateSalary1RowDialog, self).__init__(*args, **kwargs)
        self.data = list(selected_data)

        self.setWindowTitle(strs.PRESENT_VIEW_MSG)

        net_label = MyLabel(strs.PRESENT_SALARY_1_HDR[0])
        self.net_line = MyEditLine(str(selected_data[2]))
        net_label.setBuddy(self.net_line)

        gross_label = MyLabel(strs.PRESENT_SALARY_1_HDR[1])
        self.gross_line = MyEditLine(str(selected_data[3]))
        gross_label.setBuddy(self.gross_line)

        date_label = MyLabel(strs.PRESENT_SALARY_1_HDR[2])
        self.date_line = MyEditDate(selected_data[4])
        date_label.setBuddy(self.date_line)

        button_box = QDialogButtonBox(QDialogButtonBox.Yes | QDialogButtonBox.No)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        layout = QFormLayout()
        layout.addRow(net_label, self.net_line)
        layout.addRow(gross_label, self.gross_line)
        layout.addRow(date_label, self.date_line)
        layout.addRow(button_box)
        self.setLayout(layout)

    def get_value(self):
        self.data[2] = self.net_line.text()
        self.data[3] = self.gross_line.text()
        self.data[4] = self.date_line.date().toPyDate()

        return self.data


class UpdateSalary2RowDialog(QDialog):

    def __init__(self, selected_data, *args, **kwargs):
        super(UpdateSalary2RowDialog, self).__init__(*args, **kwargs)
        self.data = list(selected_data)

        self.setWindowTitle(strs.PRESENT_VIEW_MSG)

        day_label = MyLabel(strs.PRESENT_SALARY_2_HDR[1])
        self.day_line = MyEditLine(str(selected_data[3]))
        day_label.setBuddy(self.day_line)

        hour_label = MyLabel(strs.PRESENT_SALARY_2_HDR[3])
        self.hour_line = MyEditLine(str(selected_data[5]))
        hour_label.setBuddy(self.hour_line)

        meal_label = MyLabel(strs.PRESENT_SALARY_2_HDR[5])
        self.meal_line = MyEditLine(str(selected_data[7]))
        meal_label.setBuddy(self.meal_line)

        payment_label = MyLabel(strs.PRESENT_SALARY_2_HDR[7])
        self.payment_line = MyEditLine(str(selected_data[9]))
        payment_label.setBuddy(self.payment_line)

        vacation_label = MyLabel(strs.PRESENT_SALARY_2_HDR[8])
        self.vacation_line = MyEditLine(str(selected_data[10]))
        vacation_label.setBuddy(self.vacation_line)

        vacation_value_label = MyLabel(strs.PRESENT_SALARY_2_HDR[9])
        self.vacation_value_line = MyEditLine(str(selected_data[11]))
        vacation_value_label.setBuddy(self.vacation_value_line)

        fix_label = MyLabel(strs.PRESENT_SALARY_2_HDR[10])
        self.fix_line = MyEditLine(str(selected_data[12]))
        fix_label.setBuddy(self.fix_line)

        date_label = MyLabel(strs.PRESENT_SALARY_2_HDR[0])
        self.date_line = MyEditDate(selected_data[2])
        date_label.setBuddy(self.date_line)

        button_box = QDialogButtonBox(QDialogButtonBox.Yes | QDialogButtonBox.No)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        layout = QFormLayout()
        layout.addRow(day_label, self.day_line)
        layout.addRow(hour_label, self.hour_line)
        layout.addRow(meal_label, self.meal_line)
        layout.addRow(payment_label, self.payment_line)
        layout.addRow(vacation_label, self.vacation_line)
        layout.addRow(vacation_value_label, self.vacation_value_line)
        layout.addRow(fix_label, self.fix_line)
        layout.addRow(date_label, self.date_line)
        layout.addRow(button_box)
        self.setLayout(layout)

    def get_value(self):
        self.data[2] = self.date_line.date().toPyDate()
        self.data[3] = self.day_line.text()
        self.data[5] = self.hour_line.text()
        self.data[7] = self.meal_line.text()
        self.data[9] = self.payment_line.text()
        self.data[10] = self.vacation_line.text()
        self.data[11] = self.vacation_value_line.text()
        self.data[12] = self.fix_line.text()

        return self.data
