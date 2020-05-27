from PyQt5.QtWidgets import QWidget
from abc import abstractmethod


class PresentView(QWidget):

    @abstractmethod
    def _init_ui(self):
        pass

    @abstractmethod
    def _update(self):
        pass

    @abstractmethod
    def _delete(self):
        pass

    @abstractmethod
    def _print(self):
        pass

    @abstractmethod
    def get_name(self):
        pass
