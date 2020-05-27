from PyQt5.QtWidgets import *

from project.utils import constants as cons


class MyTab(QTabWidget):

    def __init__(self, *args, **kwargs):
        super(MyTab, self).__init__(*args, **kwargs)

        self.setFont(cons.TABS_FONT)
        self.resize(cons.MIN_TAB_WIDTH, cons.MIN_TAB_HEIGHT)


class MyLabel(QLabel):

    def __init__(self, text, is_required=False, *args, **kwargs):
        super(MyLabel, self).__init__(*args, **kwargs)

        self.setText(f"{text}:")
        self.setFixedSize(cons.LABELS_WIDTH, cons.LABELS_HEIGHT)
        self.setFont(cons.LABELS_FONT)

        if is_required:
            self.setStyleSheet(cons.LABEL_REQ_FLD_STYLE)


class MyEditLine(QLineEdit):

    def __init__(self, *args, **kwargs):
        super(MyEditLine, self).__init__(*args, **kwargs)

        self.setFixedSize(cons.LINES_WIDTH, cons.LINES_HEIGHT)
        self.setFont(cons.LINES_FONT)


class MyComboBox(QComboBox):

    def __init__(self, *args, **kwargs):
        super(MyComboBox, self).__init__(*args, **kwargs)

        self.setFixedSize(cons.LINES_WIDTH, cons.LINES_HEIGHT)
        self.setFont(cons.LINES_FONT)


class MyEditDate(QDateEdit):

    def __init__(self, date=cons.DEFAULT_END_DATE, *args, **kwargs):
        super(MyEditDate, self).__init__(*args, **kwargs)

        self.setFixedSize(cons.LINES_WIDTH, cons.LINES_HEIGHT)
        self.setFont(cons.LINES_FONT)
        self.setDate(date)
        self.setDisplayFormat(cons.DATE_FORMAT_PYQT)


class MyButton(QPushButton):

    def __init__(self, text, *args, **kwargs):
        super(MyButton, self).__init__(*args, **kwargs)

        self.setText(f"{text}:")
        self.setFixedSize(cons.BUTTONS_WIDTH, cons.BUTTONS_HEIGHT)
        self.setFont(cons.BUTTONS_FONT)

