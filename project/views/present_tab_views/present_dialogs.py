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

        self.setWindowTitle(strs.PRESENT_MSG)
        self.resize(cons.DIALOG_WIDTH, cons.DIALOG_HEIGHT)

        self.question_label = QLabel(self)
        self.question_label.setText("Privremeni tekst")

        button_box = QDialogButtonBox(QDialogButtonBox.Yes | QDialogButtonBox.No)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        layout = QVBoxLayout()
        layout.addWidget(self.question_label)
        layout.addWidget(button_box)
        self.setLayout(layout)

