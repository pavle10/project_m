from PyQt5.QtWidgets import *

from project.utils import constants as cons, strings as strs


class DeleteRowDialog(QDialog):

    def __init__(self, *args, **kwargs):
        super(DeleteRowDialog, self).__init__(*args, **kwargs)

        self.setWindowTitle(strs.PRESENT_MSG)
        self.resize(cons.DIALOG_WIDTH, cons.DIALOG_HEIGHT)

        question_label = QLabel(self)
        question_label.setText(strs.SALARY_2_DEL_DIALOG_MSG)

        button_box = QDialogButtonBox(QDialogButtonBox.Yes | QDialogButtonBox.No)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        layout = QVBoxLayout()
        layout.addWidget(question_label)
        layout.addWidget(button_box)
        self.setLayout(layout)


class UpdateRowDialog(QDialog):

    def __init__(self, selected_data, *args, **kwargs):
        super(UpdateRowDialog, self).__init__(*args, **kwargs)
        self.data = list(selected_data)

        self.setWindowTitle(strs.PRESENT_MSG)

        day_label = QLabel(self)
        day_label.setText("Radnih dana:")
        self.day_line = QLineEdit(self)
        self.day_line.setText(str(selected_data[3]))
        day_label.setBuddy(self.day_line)

        hour_label = QLabel(self)
        hour_label.setText("Radnih sati:")
        self.hour_line = QLineEdit(self)
        self.hour_line.setText(str(selected_data[5]))
        hour_label.setBuddy(self.hour_line)

        meal_label = QLabel(self)
        meal_label.setText("Obroka:")
        self.meal_line = QLineEdit(self)
        self.meal_line.setText(str(selected_data[7]))
        meal_label.setBuddy(self.meal_line)

        payment_label = QLabel(self)
        payment_label.setText("Rate:")
        self.payment_line = QLineEdit(self)
        self.payment_line.setText(str(selected_data[9]))
        payment_label.setBuddy(self.payment_line)

        vacation_label = QLabel(self)
        vacation_label.setText("Dana odmora:")
        self.vacation_line = QLineEdit(self)
        self.vacation_line.setText(str(selected_data[10]))
        vacation_label.setBuddy(self.vacation_line)

        vacation_value_label = QLabel(self)
        vacation_value_label.setText("Odmor vrednost:")
        self.vacation_value_line = QLineEdit(self)
        self.vacation_value_line.setText(str(selected_data[11]))
        vacation_value_label.setBuddy(self.vacation_value_line)

        fix_label = QLabel(self)
        fix_label.setText("Fiksno:")
        self.fix_line = QLineEdit(self)
        self.fix_line.setText(str(selected_data[12]))
        fix_label.setBuddy(self.fix_line)

        date_label = QLabel(self)
        date_label.setText("Datum:")
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

