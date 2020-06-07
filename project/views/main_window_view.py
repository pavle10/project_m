from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from project.utils import strings as strs, constants as cons
from project.views.tab_view.add_tab_view import AddTab
from project.views.tab_view.present_tab_view import PresentTab
from project.models.my_widgets import MyTab


class MainWind(QMainWindow):

    def __init__(self, manager, *args, **kwargs):
        super(MainWind, self).__init__(*args, **kwargs)
        self._view_manager = manager

        self._init_ui()

    def _init_ui(self):
        self.setWindowTitle(strs.WINDOWS_TITLE)
        self.setWindowIcon(QIcon(cons.APP_ICON_PATH))

        self.setWindowState(Qt.WindowMaximized)
        self._center()

        layout = QVBoxLayout()

        add_tab = AddTab(self._view_manager)
        present_tab = PresentTab(self._view_manager)

        self.tabs = MyTab()
        self.tabs.addTab(add_tab, add_tab.get_name())
        self.tabs.addTab(present_tab, present_tab.get_name())
        self.setCentralWidget(self.tabs)

        self.status_bar = QStatusBar()
        status_bar_label = QLabel(strs.ACTIVE_USER.format(user=self._view_manager.get_username()))
        status_bar_label.setFont(cons.STATUS_BAR_FONT)
        self.status_bar.addWidget(status_bar_label)

        layout.addWidget(self.tabs)
        self.setLayout(layout)
        self.setStatusBar(self.status_bar)

    def _center(self):
        frame_geometry = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frame_geometry.moveCenter(centerPoint)
        self.move(frame_geometry.topLeft())

    def update_tabs_views(self):
        for tab in self.tabs.get_tabs():
            tab.update_views()
