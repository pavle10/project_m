from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont

import project.utils.constants as cons
import project.utils.strings as strs


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

    def _center(self):
        frame_geometry = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frame_geometry.moveCenter(centerPoint)
        self.move(frame_geometry.topLeft())
