from PyQt5.QtCore import Qt

from project.views.tab_view.present_tab_views.present_dialogs import *
from project.utils.enums import Actions, Responses
from project.utils import strings as strs, funcs


class PresentUniformPieceView(QWidget):

    def __init__(self, name, manager, *args, **kwargs):
        super(PresentUniformPieceView, self).__init__(*args, **kwargs)
        self._name = name
        self._manager = manager

        self._uniform_pieces = None

        self._init_ui()

    def _init_ui(self):
        employee_label = QLabel(self)
        employee_label.setText(strs.EMPLOYEE_LBL)
        self.employee_box = QComboBox()
        self.employee_box.insertItem(0, strs.EMPTY)
        for index, employee in enumerate(self._get_employees()):
            self.employee_box.insertItem(index + 1, funcs.employee_unique_name(employee))
        self.employee_box.currentTextChanged.connect(self._change_label)
        employee_label.setBuddy(self.employee_box)

        start_date_label = QLabel(self)
        start_date_label.setText(strs.FROM_DATE_LBL)
        self.start_date_line = QDateEdit(self)
        self.start_date_line.setDate(cons.DEFAULT_START_DATE)
        self.start_date_line.setDisplayFormat(cons.DATE_FORMAT_PYQT)
        start_date_label.setBuddy(self.start_date_line)

        end_date_label = QLabel(self)
        end_date_label.setText(strs.TO_DATE_LBL)
        self.end_date_line = QDateEdit(self)
        self.end_date_line.setDate(cons.DEFAULT_END_DATE)
        self.end_date_line.setDisplayFormat(cons.DATE_FORMAT_PYQT)
        end_date_label.setBuddy(self.end_date_line)

        fields_layout = QFormLayout()
        fields_layout.addRow(employee_label, self.employee_box)
        fields_layout.addRow(start_date_label, self.start_date_line)
        fields_layout.addRow(end_date_label, self.end_date_line)

        self.table = QTableWidget()
        self.table.setColumnCount(len(strs.PRESENT_UNIFORM_PIECE_HDR))
        self.table.setHorizontalHeaderLabels(strs.PRESENT_UNIFORM_PIECE_HDR)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidget(self.table)

        update_button = QPushButton(self)
        update_button.setText(strs.UPDATE_BTN)
        update_button.clicked.connect(self._update_uniform_piece)

        delete_button = QPushButton(self)
        delete_button.setText(strs.DELETE_BTN)
        delete_button.clicked.connect(self._delete_uniform_piece)

        print_button = QPushButton(self)
        print_button.setText(strs.PRINT_BTN)
        print_button.clicked.connect(self._print_uniform_piece)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(update_button)
        buttons_layout.addWidget(delete_button)
        buttons_layout.addWidget(print_button)

        layout = QVBoxLayout()
        layout.addLayout(fields_layout)
        layout.addWidget(self.scroll_area)
        layout.addLayout(buttons_layout)
        self.setLayout(layout)

    def _get_employees(self):
        return self._manager.actions(Actions.all_employees)

    def _change_label(self):
        # Get data
        values = [self.employee_box.currentText(), self.start_date_line.date(), self.end_date_line.date()]

        self._uniform_pieces = self._manager.actions(Actions.employee_uniform_pieces, values)

        self.table.setRowCount(len(self._uniform_pieces))

        # Data rows
        for row, uniform_piece in enumerate(self._uniform_pieces):
            date = uniform_piece.get_date().strftime(cons.DATE_FORMAT_PYTHON)

            self.table.setItem(row, 0, QTableWidgetItem(uniform_piece.get_uniform_name()))
            self.table.setItem(row, 1, QTableWidgetItem(str(uniform_piece.get_size())))
            self.table.setItem(row, 2, QTableWidgetItem(str(uniform_piece.get_quantity())))
            self.table.setItem(row, 3, QTableWidgetItem(uniform_piece.get_additional()))
            self.table.setItem(row, 4, QTableWidgetItem(date))

    def keyReleaseEvent(self, event):
        if event.key() in [Qt.Key_Enter, Qt.Key_Return] and isinstance(self.focusWidget(), QDateEdit):
            self._change_label()

    def _update_uniform_piece(self):
        row_index = self._check_selection()

        if row_index is not None:
            piece = self._uniform_pieces[row_index]
            values = [piece.get_uniform_piece_id(), piece.get_uniform_id(), piece.get_employee_id(),
                      piece.get_size(), piece.get_quantity(), piece.get_additional(), piece.get_date()]
            uniforms = self._manager.actions(Actions.all_uniforms)

            dialog = UpdateUniformPieceDialog(values, uniforms)

            if dialog.exec():
                new_values = dialog.get_value()

                response = self._manager.actions(Actions.update_uniform_piece, new_values)

                if response == Responses.success:
                    QMessageBox.information(self, strs.PRESENT_VIEW_MSG, strs.UNIFORM_PIECE_UPD_SUCC_MSG)
                    self._change_label()
                else:
                    QMessageBox.warning(self, strs.PRESENT_VIEW_MSG, strs.UNIFORM_PIECE_UPD_FAIL_MSG)

    def _delete_uniform_piece(self):
        row_index = self._check_selection()

        if row_index is not None:
            dialog = DeleteRowDialog(self)

            if dialog.exec():
                values = [self._uniform_pieces[row_index].get_uniform_piece_id()]

                response = self._manager.actions(Actions.delete_uniform_piece, values)

                if response == Responses.success:
                    QMessageBox.information(self, strs.PRESENT_VIEW_MSG, strs.UNIFORM_PIECE_DEL_SUCC_MSG)
                    self._change_label()
                else:
                    QMessageBox.warning(self, strs.PRESENT_VIEW_MSG, strs.UNIFORM_PIECE_DEL_FAIL_MSG)

    def _print_uniform_piece(self):
        QMessageBox.warning(self, strs.PRESENT_VIEW_MSG, strs.NOT_IMPLEMENTED_MSG)

    def _check_selection(self):
        selected_ranges = self.table.selectedRanges()

        if len(self.table.selectedItems()) != 5 or len(selected_ranges) != 1 or selected_ranges[0].rowCount() != 1:
            QMessageBox.warning(self, strs.PRESENT_VIEW_MSG, strs.MUST_SELECT_ONE_ROW_MSG)
            self.table.clearSelection()

            return None

        return selected_ranges[0].topRow()

    def get_name(self):
        return self._name
