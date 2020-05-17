from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import *

import project.utils.constants as cons
import project.utils.strings as strs
from project.enums.actions import Actions


class LoginView(QWidget):

    def __init__(self, manager, *args, **kwargs):
        super(LoginView, self).__init__(*args, **kwargs)
        self.view_manager = manager

        self._init_ui()

    def _init_ui(self):
        self.setWindowTitle(strs.WINDOWS_TITLE)
        self.setWindowIcon(QIcon(cons.APP_ICON_PATH))

        self.setFixedSize(cons.LOGIN_WIN_WIDTH, cons.LOGIN_WIN_HEIGHT)
        self._center()

        grid_layout = QGridLayout()

        username_label = QLabel(self)
        username_label.setText(strs.USERNAME_LABEL)
        username_label.setFont(QFont("Times", pointSize=13, weight=QFont.Normal))
        grid_layout.addWidget(username_label, 0, 0)

        self.username_line = QLineEdit(self)
        username_label.setBuddy(self.username_line)
        grid_layout.addWidget(self.username_line, 0, 1)

        password_label = QLabel(self)
        password_label.setText(strs.PASSWORD_LABEL)
        password_label.setFont(QFont("Times", pointSize=13, weight=QFont.Normal))
        grid_layout.addWidget(password_label, 1, 0)

        self.password_line = QLineEdit(self)
        self.password_line.setEchoMode(QLineEdit.Password)
        password_label.setBuddy(self.password_line)
        grid_layout.addWidget(self.password_line, 1, 1)

        login_button = QPushButton(self)
        login_button.setText(strs.LOGIN_BUTTON)
        login_button.clicked.connect(lambda x: self.view_manager.actions(Actions.login,
                                                                         [self.username_line.text(),
                                                                          self.password_line.text()]))
        grid_layout.addWidget(login_button, 2, 1)

        group_box = QGroupBox(strs.MAIN_LABEL)
        group_box.setFont(QFont("Times", pointSize=15, weight=QFont.Normal))
        group_box.setLayout(grid_layout)
        group_box.setFixedSize(400, 400)
        group_box.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(group_box)
        layout.setAlignment(Qt.AlignCenter)
        self.setLayout(layout)

    def _center(self):
        frame_geometry = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frame_geometry.moveCenter(centerPoint)
        self.move(frame_geometry.topLeft())

    def _clear(self):
        self.username_line.clear()
        self.password_line.clear()

    def failed_login(self):
        QMessageBox.warning(self, strs.FAILED_LOGIN_TITLE, strs.FAILED_LOGIN_MSG)

        self._clear()

    def successful_login(self, username):
        QMessageBox.information(self, strs.SUCCESSFUL_LOGIN_TITLE, strs.SUCCESSFUL_LOGIN_MSG+username)
