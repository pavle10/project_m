from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

import project.utils.strings as strs
import project.utils.funcs as funcs
from project.views.add_tab.add_employee_view import AddEmployeeView
from project.views.add_tab.add_position_view import AddPositionView
from project.views.add_tab.add_uniform_view import AddUniformView
from project.views.add_tab.add_uniform_piece_view import AddUniformPieceView
from project.views.add_tab.add_child_view import AddChildView
from project.views.add_tab.add_free_days_view import AddFreeDaysView
from project.views.add_tab.add_wage_view import AddWageView
from project.views.add_tab.add_salary_1_view import AddSalary1View
from project.views.add_tab.add_salary_2_view import AddSalary2View


class AddTab(QWidget):

    def __init__(self, manager, *args, **kwargs):
        super(AddTab, self).__init__(*args, **kwargs)
        self._name = strs.ADD_TAB_NAME
        self._manager = manager

        self._init_ui()

    def _init_ui(self):
        self.options_list = QListWidget(self)
        for value in funcs.data_manipulation_options():
            self.options_list.insertItem(value[0], value[1])
        self.options_list.clicked.connect(self._change_view)

        scroll_area = QScrollArea(self)
        scroll_area.setWidget(self.options_list)

        add_employee = AddEmployeeView(self._manager)
        add_position = AddPositionView(self._manager)
        add_child = AddChildView(self._manager)
        add_uniform = AddUniformView(self._manager)
        add_uniform_piece = AddUniformPieceView(self._manager)
        add_free_days = AddFreeDaysView(self._manager)
        add_wage = AddWageView(self._manager)
        add_salary_1 = AddSalary1View(self._manager)
        add_salary_2 = AddSalary2View(self._manager)

        self.views = list()
        self.views.append(add_employee)
        self.views.append(add_position)
        self.views.append(add_child)
        self.views.append(add_uniform)
        self.views.append(add_uniform_piece)
        self.views.append(add_free_days)
        self.views.append(add_wage)
        self.views.append(add_salary_1)
        self.views.append(add_salary_2)

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





