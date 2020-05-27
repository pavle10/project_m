from project.views.tab_view.present_tab_views.present_dialogs import *
from project.utils.enums import Actions, Responses
from project.utils import strings as strs


class PresentEmployeeView(QWidget):

    def __init__(self, name, manager, *args, **kwargs):
        super(PresentEmployeeView, self).__init__(*args, **kwargs)
        self._name = name
        self._manager = manager

        self._init_ui()

    def _init_ui(self):
        self.table = QTableWidget()
        self.table.setColumnCount(len(strs.PRESENT_EMPLOYEE_HDR))
        self.table.setHorizontalHeaderLabels(strs.PRESENT_EMPLOYEE_HDR)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.update_table()

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidget(self.table)

        update_button = QPushButton(self)
        update_button.setText(strs.UPDATE_BTN)
        update_button.clicked.connect(self._update_employee)

        delete_button = QPushButton(self)
        delete_button.setText(strs.DELETE_BTN)
        delete_button.clicked.connect(self._delete_employee)

        print_button = QPushButton(self)
        print_button.setText(strs.PRINT_BTN)
        print_button.clicked.connect(self._print_employee)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(update_button)
        buttons_layout.addWidget(delete_button)
        buttons_layout.addWidget(print_button)

        layout = QVBoxLayout()
        layout.addWidget(self.scroll_area)
        layout.addLayout(buttons_layout)
        self.setLayout(layout)

    def update_table(self):
        self.employees = self._manager.actions(Actions.all_employees)
        positions = self._manager.actions(Actions.all_positions)

        self.table.setRowCount(len(self.employees))

        for row, employee in enumerate(self.employees):
            position_name = ""
            for position in positions:
                if position.get_position_id() == employee.get_position():
                    position_name = position.get_name()
                    break

            self.table.setItem(row, 0, QTableWidgetItem(employee.get_first_name()))
            self.table.setItem(row, 1, QTableWidgetItem(employee.get_last_name()))
            self.table.setItem(row, 2, QTableWidgetItem(employee.get_fathers_name()))
            self.table.setItem(row, 3, QTableWidgetItem(employee.get_identity_number()))
            self.table.setItem(row, 4, QTableWidgetItem(employee.get_personal_card()))
            self.table.setItem(row, 5, QTableWidgetItem(employee.get_qualification()))
            self.table.setItem(row, 6, QTableWidgetItem(position_name))
            self.table.setItem(row, 7, QTableWidgetItem(employee.get_saint_day()))
            self.table.setItem(row, 8, QTableWidgetItem(employee.get_address()))
            self.table.setItem(row, 9, QTableWidgetItem(employee.get_account()))
            self.table.setItem(row, 10, QTableWidgetItem(employee.get_before_m()))
            self.table.setItem(row, 11, QTableWidgetItem(employee.get_start_date().strftime(cons.DATE_FORMAT_PYTHON)))
            self.table.setItem(row, 12, QTableWidgetItem(employee.get_home_number()))
            self.table.setItem(row, 13, QTableWidgetItem(employee.get_mobile_number()))
            self.table.setItem(row, 14, QTableWidgetItem(employee.get_situation()))

    def _update_employee(self):
        row_index = self._check_selection()

        if row_index is not None:
            employee = self.employees[row_index]
            positions = self._manager.actions(Actions.all_positions)

            dialog = UpdateEmployeeDialog(employee.data_to_array(), positions)

            if dialog.exec():
                response = self._manager.actions(Actions.update_employee, dialog.get_value())

                if response == Responses.success:
                    QMessageBox.information(self, strs.PRESENT_VIEW_MSG, strs.EMPLOYEE_UPD_SUCC_MSG)
                    self.update_table()
                else:
                    QMessageBox.warning(self, strs.PRESENT_VIEW_MSG, strs.EMPLOYEE_UPD_FAIL_MSG)

    def _delete_employee(self):
        row_index = self._check_selection()

        if row_index is not None:
            dialog = DeleteRowDialog()

            if dialog.exec():
                employee = self.employees[row_index]

                response = self._manager.actions(Actions.delete_employee, [employee.get_employee_id()])

                if response == Responses.success:
                    QMessageBox.information(self, strs.PRESENT_VIEW_MSG, strs.EMPLOYEE_DEL_SUCC_MSG)
                    self.update_table()
                else:
                    QMessageBox.warning(self, strs.PRESENT_VIEW_MSG, strs.EMPLOYEE_DEL_FAIL_MSG)

    def _print_employee(self):
        QMessageBox.warning(self, strs.PRESENT_VIEW_MSG, strs.NOT_IMPLEMENTED_MSG)

    def _check_selection(self):
        selected_ranges = self.table.selectedRanges()

        if len(self.table.selectedItems()) != 15 or len(selected_ranges) != 1 or selected_ranges[0].rowCount() != 1:
            QMessageBox.warning(self, strs.PRESENT_VIEW_MSG, strs.MUST_SELECT_ONE_ROW_MSG)
            self.table.clearSelection()

            return None

        return selected_ranges[0].topRow()

    def get_name(self):
        return self._name
