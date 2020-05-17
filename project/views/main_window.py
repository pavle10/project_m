from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont

import project.utils.constants as cons
import project.utils.strings as strs
from project.views.add_tab.add__tab import AddTab
from project.enums.actions import Actions


class MainWind(QMainWindow):

    def __init__(self, manager, *args, **kwargs):
        super(MainWind, self).__init__(*args, **kwargs)
        self._view_manager = manager

        self._init_ui()

    def _init_ui(self):
        self.setWindowTitle(strs.WINDOWS_TITLE)
        self.setWindowIcon(QIcon(cons.APP_ICON_PATH))

        self.setFixedSize(cons.MAIN_WIN_WIDTH, cons.MAIN_WIN_HEIGHT)
        self._center()

        layout = QVBoxLayout()
        tabs = QTabWidget()
        tabs.resize(cons.MIN_TAB_WIDTH, cons.MIN_TAB_HEIGHT)
        tabs.addTab(AddTab(self._view_manager), strs.ADD_TAB_NAME)
        self.setCentralWidget(tabs)

        layout.addWidget(tabs)
        self.setLayout(layout)

    def _center(self):
        frame_geometry = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frame_geometry.moveCenter(centerPoint)
        self.move(frame_geometry.topLeft())

    def add_position(self, values):
        self._view_manager.actions(Actions.add_employee, values)
