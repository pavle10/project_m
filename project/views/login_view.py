from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from project.utils.constants import ICONS_PATH, IMAGES_PATH


class LoginView(QWidget):

    def __init__(self, *args, **kwargs):
        super(LoginView, self).__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Login")
        self.setWindowIcon(QIcon(ICONS_PATH + "/app_icon.png"))

        self.setBaseSize(600, 500)
        self.center()

        layout = QVBoxLayout()

        login_image_label = QLabel(self)
        login_image = QPixmap(IMAGES_PATH + "/login.png")
        login_image_label.setPixmap(login_image)
        #login_image_label.setScaledContents(True)
        layout.addWidget(login_image_label)

        self.setLayout(layout)

    def center(self):
        frame_geometry = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frame_geometry.moveCenter(centerPoint)
        self.move(frame_geometry.topLeft())
