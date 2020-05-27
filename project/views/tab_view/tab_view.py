from PyQt5.QtWidgets import QWidget
from abc import abstractmethod


class TabView(QWidget):

    @abstractmethod
    def _init_ui(self):
        pass

    @abstractmethod
    def _change_view(self):
        pass

    @abstractmethod
    def get_name(self):
        pass
