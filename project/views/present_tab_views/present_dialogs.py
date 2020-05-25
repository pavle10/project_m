from PyQt5.QtWidgets import *

from project.utils import constants as cons, strings as strs


class DeleteRowDialog(QDialog):

    def __init__(self, *args, **kwargs):
        super(DeleteRowDialog, self).__init__(*args, **kwargs)

        self.setWindowTitle(strs.PRESENT_MSG)
        self.resize(cons.DIALOG_WIDTH, cons.DIALOG_HEIGHT)

        question_label = QLabel(self)
        question_label.setText(strs.DELETE_DIALOG_MSG)

        button_box = QDialogButtonBox(QDialogButtonBox.Yes | QDialogButtonBox.No)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        layout = QVBoxLayout()
        layout.addWidget(question_label)
        layout.addWidget(button_box)
        self.setLayout(layout)


class UpdateFreeDaysRowDialog(QDialog):

    def __init__(self, selected_data, *args, **kwargs):
        super(UpdateFreeDaysRowDialog, self).__init__(*args, **kwargs)
        self.data = selected_data

        self.setWindowTitle(strs.PRESENT_MSG)

        start_date_label = QLabel(self)
        start_date_label.setText(strs.PRESENT_FREE_DAYS_HDR[0])
        self.start_date_line = QDateEdit(self)
        self.start_date_line.setDate(selected_data[2])
        start_date_label.setBuddy(self.start_date_line)

        end_date_label = QLabel(self)
        end_date_label.setText(strs.PRESENT_FREE_DAYS_HDR[1])
        self.end_date_line = QDateEdit(self)
        self.end_date_line.setDate(selected_data[3])
        end_date_label.setBuddy(self.end_date_line)

        reason_label = QLabel(self)
        reason_label.setText(strs.PRESENT_FREE_DAYS_HDR[2])
        self.reason_line = QLineEdit(self)
        self.reason_line.setText(selected_data[5])
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
        self.data[4] = (self.data[3] - self.data[2]).days
        self.data[5] = self.reason_line.text()

        return self.data


class UpdateWageRowDialog(QDialog):

    def __init__(self, selected_data, *args, **kwargs):
        super(UpdateWageRowDialog, self).__init__(*args, **kwargs)
        self.data = selected_data

        self.setWindowTitle(strs.PRESENT_MSG)

        day_label = QLabel(self)
        day_label.setText(strs.PRESENT_WAGE_HDR[0])
        self.day_line = QLineEdit(self)
        self.day_line.setText(str(selected_data[2]))
        day_label.setBuddy(self.day_line)

        hour_label = QLabel(self)
        hour_label.setText(strs.PRESENT_WAGE_HDR[1])
        self.hour_line = QLineEdit(self)
        self.hour_line.setText(str(selected_data[3]))
        hour_label.setBuddy(self.hour_line)

        meal_label = QLabel(self)
        meal_label.setText(strs.PRESENT_WAGE_HDR[2])
        self.meal_line = QLineEdit(self)
        self.meal_line.setText(str(selected_data[4]))
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

        self.setWindowTitle(strs.PRESENT_MSG)

        net_label = QLabel(self)
        net_label.setText(strs.PRESENT_SALARY_1_HDR[0])
        self.net_line = QLineEdit(self)
        self.net_line.setText(str(selected_data[2]))
        net_label.setBuddy(self.net_line)

        gross_label = QLabel(self)
        gross_label.setText(strs.PRESENT_SALARY_1_HDR[1])
        self.gross_line = QLineEdit(self)
        self.gross_line.setText(str(selected_data[3]))
        gross_label.setBuddy(self.gross_line)

        date_label = QLabel(self)
        date_label.setText(strs.PRESENT_SALARY_1_HDR[2])
        self.date_line = QDateEdit(self)
        self.date_line.setDate(selected_data[4])
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

        self.setWindowTitle(strs.PRESENT_MSG)

        day_label = QLabel(self)
        day_label.setText(strs.PRESENT_SALARY_2_HDR[3])
        self.day_line = QLineEdit(self)
        self.day_line.setText(str(selected_data[3]))
        day_label.setBuddy(self.day_line)

        hour_label = QLabel(self)
        hour_label.setText(strs.PRESENT_SALARY_2_HDR[5])
        self.hour_line = QLineEdit(self)
        self.hour_line.setText(str(selected_data[5]))
        hour_label.setBuddy(self.hour_line)

        meal_label = QLabel(self)
        meal_label.setText(strs.PRESENT_SALARY_2_HDR[7])
        self.meal_line = QLineEdit(self)
        self.meal_line.setText(str(selected_data[7]))
        meal_label.setBuddy(self.meal_line)

        payment_label = QLabel(self)
        payment_label.setText(strs.PRESENT_SALARY_2_HDR[9])
        self.payment_line = QLineEdit(self)
        self.payment_line.setText(str(selected_data[9]))
        payment_label.setBuddy(self.payment_line)

        vacation_label = QLabel(self)
        vacation_label.setText(strs.PRESENT_SALARY_2_HDR[10])
        self.vacation_line = QLineEdit(self)
        self.vacation_line.setText(str(selected_data[10]))
        vacation_label.setBuddy(self.vacation_line)

        vacation_value_label = QLabel(self)
        vacation_value_label.setText(strs.PRESENT_SALARY_2_HDR[11])
        self.vacation_value_line = QLineEdit(self)
        self.vacation_value_line.setText(str(selected_data[11]))
        vacation_value_label.setBuddy(self.vacation_value_line)

        fix_label = QLabel(self)
        fix_label.setText(strs.PRESENT_SALARY_2_HDR[12])
        self.fix_line = QLineEdit(self)
        self.fix_line.setText(str(selected_data[12]))
        fix_label.setBuddy(self.fix_line)

        date_label = QLabel(self)
        date_label.setText(strs.PRESENT_SALARY_2_HDR[2])
        self.date_line = QDateEdit(self)
        self.date_line.setDate(selected_data[2])
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
