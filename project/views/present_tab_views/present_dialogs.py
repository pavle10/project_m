from PyQt5.QtWidgets import *

from project.utils.constants import *


class DeleteRowDialog(QDialog):

    def __init__(self, *args, **kwargs):
        super(DeleteRowDialog, self).__init__(*args, **kwargs)

        self.setWindowTitle("Prikaz dialog")
        self.resize(DIALOG_WIDTH, DIALOG_HEIGHT)

        question_label = QLabel(self)
        question_label.setText("Da li si sigurna da želiš da izbrišeš ovaj red?")

        button_box = QDialogButtonBox(QDialogButtonBox.Yes | QDialogButtonBox.No)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        layout = QVBoxLayout()
        layout.addWidget(question_label)
        layout.addWidget(button_box)
        self.setLayout(layout)
