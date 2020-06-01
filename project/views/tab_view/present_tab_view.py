from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from project.views.tab_view.present_tab_views.present_employee_view import PresentEmployeeView
from project.views.tab_view.present_tab_views.present_position_view import PresentPositionView
from project.views.tab_view.present_tab_views.present_child_view import PresentChildView
from project.views.tab_view.present_tab_views.present_uniform_view import PresentUniformView
from project.views.tab_view.present_tab_views.present_uniform_piece_view import PresentUniformPieceView
from project.views.tab_view.present_tab_views.present_free_days_view import PresentFreeDaysView
from project.views.tab_view.present_tab_views.present_wage_view import PresentWageView
from project.views.tab_view.present_tab_views.present_salary_1_view import PresentSalary1View
from project.views.tab_view.present_tab_views.present_salary_2_view import PresentSalary2View
from project.utils import strings as strs, constants as cons
from project.views.tab_view.tab_view import TabView
from project.models.my_widgets import MyList


class PresentTab(TabView):

    def __init__(self, manager, *args, **kwargs):
        super(PresentTab, self).__init__(*args, **kwargs)
        self._name = strs.PRESENT_TAB_NAME
        self._manager = manager

        self._init_ui()

    def _init_ui(self):
        present_employee_view = PresentEmployeeView(strs.EMPLOYEE, self._manager)
        present_position_view = PresentPositionView(strs.POSITION, self._manager)
        present_child_view = PresentChildView(strs.CHILD, self._manager)
        present_uniform_view = PresentUniformView(strs.UNIFORM, self._manager)
        present_uniform_piece_view = PresentUniformPieceView(strs.UNIFORM_PIECE, self._manager)
        present_free_days_view = PresentFreeDaysView(strs.FREE_DAY, self._manager)
        present_wage_view = PresentWageView(strs.WAGE, self._manager)
        present_salary_1_view = PresentSalary1View(strs.SALARY_1, self._manager)
        present_salary_2_view = PresentSalary2View(strs.SALARY_2, self._manager)

        self.views = list()
        self.views.append(present_employee_view)
        self.views.append(present_position_view)
        self.views.append(present_child_view)
        self.views.append(present_uniform_view)
        self.views.append(present_uniform_piece_view)
        self.views.append(present_free_days_view)
        self.views.append(present_wage_view)
        self.views.append(present_salary_1_view)
        self.views.append(present_salary_2_view)

        self.options_list = MyList(self.views)
        self.options_list.clicked.connect(self._change_view)

        scroll_area = QScrollArea(self)
        scroll_area.setFixedSize(cons.SCROLL_AREA_WIDTH, cons.SCROLL_AREA_HEIGHT)
        scroll_area.setWidgetResizable(True)
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

    def update_views(self):
        for view in self.views:
            print(view.get_name())
            view.update()
