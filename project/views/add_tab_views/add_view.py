from PyQt5.QtWidgets import *
from abc import abstractmethod


class AddView(QWidget):

    @abstractmethod
    def _init_ui(self):
        pass

    @abstractmethod
    def _add(self):
        pass

    @abstractmethod
    def get_name(self):
        pass
