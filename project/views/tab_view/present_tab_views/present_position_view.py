from project.views.present_tab_views.present_dialogs import *
from project.utils.enums import Actions, Responses
from project.utils import strings as strs


class PresentPositionView(QWidget):

    def __init__(self, name, manager, *args, **kwargs):
        super(PresentPositionView, self).__init__(*args, **kwargs)
        self._name = name
        self._manager = manager

        self._init_ui()

    def _init_ui(self):
        self.table = QTableWidget()
        self.table.setColumnCount(len(strs.PRESENT_POSITION_HDR))
        self.table.setHorizontalHeaderLabels(strs.PRESENT_POSITION_HDR)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.update_table()

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidget(self.table)

        update_button = QPushButton(self)
        update_button.setText(strs.UPDATE_BTN)
        update_button.clicked.connect(self._update_position)

        delete_button = QPushButton(self)
        delete_button.setText(strs.DELETE_BTN)
        delete_button.clicked.connect(self._delete_position)

        print_button = QPushButton(self)
        print_button.setText(strs.PRINT_BTN)
        print_button.clicked.connect(self._print_position)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(update_button)
        buttons_layout.addWidget(delete_button)
        buttons_layout.addWidget(print_button)

        layout = QVBoxLayout()
        layout.addWidget(self.scroll_area)
        layout.addLayout(buttons_layout)
        self.setLayout(layout)

    def update_table(self):
        positions = self._manager.actions(Actions.all_positions)

        self.table.setRowCount(len(positions))

        for row, position in enumerate(positions):
            saturday_value = strs.YES if position.get_saturday() else strs.NO

            self.table.setItem(row, 0, QTableWidgetItem(position.get_name()))
            self.table.setItem(row, 1, QTableWidgetItem(saturday_value))

    def _update_position(self):
        row_index = self._check_selection()

        if row_index is not None:
            position_name = self.table.selectedItems()[0].text()
            saturday_value = int(not funcs.convert_saturday(self.table.selectedItems()[1].text()))
            values = [None, position_name, saturday_value]

            dialog = UpdatePositionDialog(values)

            if dialog.exec():
                response = self._manager.actions(Actions.update_position, [position_name, dialog.get_value()])

                if response == Responses.success:
                    QMessageBox.information(self, strs.PRESENT_VIEW_MSG, strs.POSITION_UPD_SUCC_MSG)
                    self.update_table()
                else:
                    QMessageBox.warning(self, strs.PRESENT_VIEW_MSG, strs.POSITION_UPD_FAIL_MSG)

    def _delete_position(self):
        row_index = self._check_selection()

        if row_index is not None:
            values = [self.table.selectedItems()[0].text()]

            dialog = DeleteRowDialog()

            if dialog.exec():
                response = self._manager.actions(Actions.delete_position, values)
                print(response)

                if response == Responses.success:
                    QMessageBox.information(self, strs.PRESENT_VIEW_MSG, strs.POSITION_DEL_SUCC_MSG)
                    self.update_table()
                else:
                    QMessageBox.warning(self, strs.PRESENT_VIEW_MSG, strs.POSITION_DEL_FAIL_MSG)

    def _print_position(self):
        QMessageBox.warning(self, strs.PRESENT_VIEW_MSG, strs.NOT_IMPLEMENTED_MSG)

    def _check_selection(self):
        selected_ranges = self.table.selectedRanges()

        if len(self.table.selectedItems()) != 2 or len(selected_ranges) != 1 or selected_ranges[0].rowCount() != 1:
            QMessageBox.warning(self, strs.PRESENT_VIEW_MSG, strs.MUST_SELECT_ONE_ROW_MSG)
            self.table.clearSelection()

            return None

        return selected_ranges[0].topRow()

    def get_name(self):
        return self._name
