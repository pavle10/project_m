from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from project.views.tab_view.tab_view import TabView
from project.models.my_widgets import MyList
from project.utils import strings as strs, constants as cons
from project.views.tab_view.add_tab_views.add_employee_view import AddEmployeeView
from project.views.tab_view.add_tab_views.add_position_view import AddPositionView
from project.views.tab_view.add_tab_views.add_uniform_view import AddUniformView
from project.views.tab_view.add_tab_views.add_uniform_piece_view import AddUniformPieceView
from project.views.tab_view.add_tab_views.add_child_view import AddChildView
from project.views.tab_view.add_tab_views.add_free_days_view import AddFreeDaysView
from project.views.tab_view.add_tab_views.add_wage_view import AddWageView
from project.views.tab_view.add_tab_views.add_salary_1_view import AddSalary1View
from project.views.tab_view.add_tab_views.add_salary_2_view import AddSalary2View


class AddTab(TabView):

    def __init__(self, manager, *args, **kwargs):
        super(AddTab, self).__init__(*args, **kwargs)
        self._name = strs.ADD_TAB_NAME
        self._manager = manager

        self._init_ui()

    def _init_ui(self):
        add_employee = AddEmployeeView(strs.EMPLOYEE, self._manager)
        add_position = AddPositionView(strs.POSITION, self._manager)
        add_child = AddChildView(strs.CHILD, self._manager)
        add_uniform = AddUniformView(strs.UNIFORM, self._manager)
        add_uniform_piece = AddUniformPieceView(strs.UNIFORM_PIECE, self._manager)
        add_free_days = AddFreeDaysView(strs.FREE_DAY, self._manager)
        add_wage = AddWageView(strs.WAGE, self._manager)
        add_salary_1 = AddSalary1View(strs.SALARY_1, self._manager)
        add_salary_2 = AddSalary2View(strs.SALARY_2, self._manager)

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

        self.options_list = MyList(self.views)
        self.options_list.clicked.connect(self._change_view)

        scroll_area = QScrollArea(self)
        scroll_area.setFixedSize(cons.SCROLL_AREA_WIDTH, cons.SCROLL_AREA_HEIGHT)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.options_list)

        self.splitter = QSplitter(Qt.Horizontal)
        self.splitter.addWidget(scroll_area)
        self.splitter.addWidget(QFrame(self.splitter))

        layout = QHBoxLayout()
        layout.addWidget(self.splitter)
        self.setLayout(layout)

    def _change_view(self):
        item = self.options_list.currentItem()
        index = int(self.options_list.indexFromItem(item).row())

        self.splitter.replaceWidget(1, self.views[index])

    def get_name(self):
        return self._name

    def update_views(self):
        for view in self.views:
            view.update()
