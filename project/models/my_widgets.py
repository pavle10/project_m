from PyQt5.QtWidgets import *

from project.utils import constants as cons


class MyTab(QTabWidget):

    def __init__(self, *args, **kwargs):
        super(MyTab, self).__init__(*args, **kwargs)
        self._tabs_list = list()

        self.setFont(cons.TABS_FONT)
        self.resize(cons.MIN_TAB_WIDTH, cons.MIN_TAB_HEIGHT)

    def addTab(self, tab, tab_name):
        QTabWidget.addTab(self, tab, tab_name)

        self._tabs_list.append(tab)

    def get_tabs(self):
        return self._tabs_list


class MyList(QListWidget):

    def __init__(self, options, *args, **kwargs):
        super(MyList, self).__init__(*args, **kwargs)

        self.setFont(cons.LIST_FONT)

        for index, option in enumerate(options):
            self.insertItem(index, option.get_name())


class MyLabel(QLabel):

    def __init__(self, text, is_required=False, *args, **kwargs):
        super(MyLabel, self).__init__(*args, **kwargs)

        self.setText(f"{text}:")
        self.setFixedSize(cons.LABELS_WIDTH, cons.LABELS_HEIGHT)
        self.setFont(cons.LABELS_FONT)

        if is_required:
            self.setStyleSheet(cons.LABEL_REQ_FLD_STYLE)


class MyLabelShort(QLabel):

    def __init__(self, text, *args, **kwargs):
        super(MyLabelShort, self).__init__(*args, **kwargs)

        self.setText(f"{text}:")
        self.setFixedSize(cons.SHORT_LABELS_WIDTH, cons.SHORT_LABELS_HEIGHT)
        self.setFont(cons.SHORT_LABELS_FONT)


class MyEditLine(QLineEdit):

    def __init__(self, text=None, *args, **kwargs):
        super(MyEditLine, self).__init__(*args, **kwargs)

        self.setFixedSize(cons.LINES_WIDTH, cons.LINES_HEIGHT)
        self.setFont(cons.LINES_FONT)

        if text:
            self.setText(text)


class MyEditLineShort(QLineEdit):

    def __init__(self, *args, **kwargs):
        super(MyEditLineShort, self).__init__(*args, **kwargs)

        self.setFixedSize(cons.SHORT_LABELS_WIDTH, cons.SHORT_LABELS_HEIGHT)
        self.setFont(cons.SHORT_LABELS_FONT)


class MyComboBox(QComboBox):

    def __init__(self, items, *args, **kwargs):
        super(MyComboBox, self).__init__(*args, **kwargs)

        self.setFixedSize(cons.LINES_WIDTH, cons.LINES_HEIGHT)
        self.setFont(cons.LINES_FONT)

        for index, item in enumerate(items):
            self.insertItem(index, item)

    def update_items(self, items):
        self.blockSignals(True)
        self.clear()

        for index, item in enumerate(items):
            self.insertItem(index, item)
        self.blockSignals(False)


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

        self.setText(f"{text}")
        self.setFixedSize(cons.BUTTONS_WIDTH, cons.BUTTONS_HEIGHT)
        self.setFont(cons.BUTTONS_FONT)


class MyTable(QTableWidget):

    def __init__(self, header=None, *args, **kwargs):
        super(MyTable, self).__init__(*args, **kwargs)

        self.setEditTriggers(QTableWidget.NoEditTriggers)

        if header:
            self.setColumnCount(len(header))
            self.setHorizontalHeaderLabels(header)


