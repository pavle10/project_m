from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

import project.utils.strings as strs
from project.views.present_tab_views.present_wage_view import PresentWageView
from .present_tab_views.present_salary_1_view import PresentSalary1View
from project.views.present_tab_views.present_salary_2_view import PresentSalary2View


class PresentTab(QWidget):

    def __init__(self, manager, *args, **kwargs):
        super(PresentTab, self).__init__(*args, **kwargs)
        self._name = strs.PRESENT_TAB_NAME
        self._manager = manager

        self._init_ui()

    def _init_ui(self):
        present_wage_view = PresentWageView(strs.WAGE, self._manager)
        present_salary_1_view = PresentSalary1View(strs.SALARY_1, self._manager)
        present_salary_2_view = PresentSalary2View(strs.SALARY_2, self._manager)

        self.views = list()
        self.views.append(present_wage_view)
        self.views.append(present_salary_1_view)
        self.views.append(present_salary_2_view)

        self.options_list = QListWidget(self)
        for index, view in enumerate(self.views):
            self.options_list.insertItem(index, view.get_name())
        self.options_list.clicked.connect(self._change_view)

        scroll_area = QScrollArea(self)
        scroll_area.setWidget(self.options_list)

        self.splitter = QSplitter(Qt.Horizontal)
        self.splitter.addWidget(scroll_area)
        self.splitter.addWidget(QFrame(self))

        layout = QHBoxLayout()
        layout.addWidget(self.splitter)
        self.setLayout(layout)

    def _change_view(self):
        item = self.options_list.currentItem()
        index = int(self.options_list.indexFromItem(item).row())

        self.splitter.replaceWidget(1, self.views[index])

    def get_name(self):
        return self._name

