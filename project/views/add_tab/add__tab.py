from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

import project.utils.strings as strs
import project.utils.funcs as funcs
from project.views.add_tab.add_employee_view import AddEmployeeView
from project.views.add_tab.add_position_view import AddPositionView
from project.views.add_tab.add_uniform_view import AddUniformView
from project.views.add_tab.add_uniform_piece_view import AddUniformPieceView
from project.views.add_tab.add_child_view import AddChildView


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

        self.views = list()
        self.views.append(add_employee)
        self.views.append(add_position)
        self.views.append(add_child)
        self.views.append(add_uniform)
        self.views.append(add_uniform_piece)

        self.splitter = QSplitter(Qt.Horizontal)
        self.splitter.addWidget(scroll_area)
        self.splitter.addWidget(QFrame(self))

        layout = QHBoxLayout()
        layout.addWidget(self.splitter)
        self.setLayout(layout)

    def _change_view(self):
        item = self.options_list.currentItem()
        index = int(self.options_list.indexFromItem(item).row())

        self.splitter.replaceWidget(1, self.views[index % len(self.views)])





