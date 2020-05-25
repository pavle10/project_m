from PyQt5.QtCore import Qt

from project.views.present_tab_views.present_dialogs import *
from project.utils.enums import Actions, Responses
from project.utils import strings as strs


class PresentUniformView(QWidget):

    def __init__(self, name, manager, *args, **kwargs):
        super(PresentUniformView, self).__init__(*args, **kwargs)
        self._name = name
        self._manager = manager

        self._init_ui()

    def _init_ui(self):
        self.table = QTableWidget()
        self.table.setColumnCount(len(strs.PRESENT_UNIFORM_HDR))
        self.table.setHorizontalHeaderLabels(strs.PRESENT_UNIFORM_HDR)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)

        self.update_table()

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidget(self.table)

        update_button = QPushButton(self)
        update_button.setText(strs.UPDATE_BTN)
        update_button.clicked.connect(self._update_uniform)

        delete_button = QPushButton(self)
        delete_button.setText(strs.DELETE_BTN)
        delete_button.clicked.connect(self._delete_uniform)

        print_button = QPushButton(self)
        print_button.setText(strs.PRINT_BTN)
        print_button.clicked.connect(self._print_uniform)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(update_button)
        buttons_layout.addWidget(delete_button)
        buttons_layout.addWidget(print_button)

        layout = QVBoxLayout()
        layout.addWidget(self.scroll_area)
        layout.addLayout(buttons_layout)
        self.setLayout(layout)

    def update_table(self):
        uniforms = self._manager.actions(Actions.all_uniforms)

        self.table.setRowCount(len(uniforms))

        for row, uniform in enumerate(uniforms):
            self.table.setItem(row, 0, QTableWidgetItem(uniform.get_name()))

    def _update_uniform(self):
        row_index = self._check_selection()

        if row_index is not None:
            values = [self.table.currentItem().text(), ""]

            dialog = UpdateUniformDialog(values)

            if dialog.exec():
                new_values = dialog.get_value()

                response = self._manager.actions(Actions.update_uniform, new_values)

                if response == Responses.success:
                    QMessageBox.information(self, strs.PRESENT_MSG, strs.UNIFORM_UPD_SUCC_MSG)
                    self.update_table()
                else:
                    QMessageBox.warning(self, strs.PRESENT_MSG, strs.UNIFORM_UPD_FAIL_MSG)

    def _delete_uniform(self):
        row_index = self._check_selection()

        if row_index is not None:
            dialog = DeleteRowDialog(self)

            if dialog.exec():
                values = [self.table.currentItem().text()]

                response = self._manager.actions(Actions.delete_uniform, values)

                if response == Responses.success:
                    QMessageBox.information(self, strs.PRESENT_MSG, strs.UNIFORM_DEL_SUCC_MSG)
                    self.update_table()
                else:
                    QMessageBox.warning(self, strs.PRESENT_MSG, strs.UNIFORM_DEL_FAIL_MSG)

    def _print_uniform(self):
        QMessageBox.warning(self, strs.PRESENT_MSG, strs.NOT_IMPLEMENTED_MSG)

    def _check_selection(self):
        selected_ranges = self.table.selectedRanges()

        if len(self.table.selectedItems()) != 1 or len(selected_ranges) != 1 or selected_ranges[0].rowCount() != 1:
            QMessageBox.warning(self, strs.PRESENT_MSG, strs.MUST_SELECT_ONE_ROW_MSG)
            self.table.clearSelection()

            return None

        return selected_ranges[0].topRow()

    def get_name(self):
        return self._name
