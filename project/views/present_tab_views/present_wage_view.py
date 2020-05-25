from PyQt5.QtCore import Qt

from project.views.present_tab_views.present_dialogs import *
from project.utils.enums import Actions, Responses
from project.utils import strings as strs, constants as cons


class PresentWageView(QWidget):

    def __init__(self, name, manager, *args, **kwargs):
        super(PresentWageView, self).__init__(*args, **kwargs)
        self._name = name
        self._manager = manager

        self._wages = None

        self._init_ui()

    def _init_ui(self):
        employee_label = QLabel(self)
        employee_label.setText(strs.EMPLOYEE_LBL)
        self.employee_box = QComboBox()
        self.employee_box.insertItem(0, strs.EMPTY)
        for index, employee in enumerate(self._get_employees()):
            self.employee_box.insertItem(index+1, f"{employee[0]} {employee[1]} {employee[2]}")
        self.employee_box.currentTextChanged.connect(self._change_label)
        employee_label.setBuddy(self.employee_box)

        fields_layout = QFormLayout()
        fields_layout.addRow(employee_label, self.employee_box)

        self.table = QTableWidget()
        self.table.setColumnCount(len(strs.PRESENT_WAGE_HDR))
        self.table.setHorizontalHeaderLabels(strs.PRESENT_WAGE_HDR)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidget(self.table)

        update_button = QPushButton(self)
        update_button.setText(strs.UPDATE_BTN)
        update_button.clicked.connect(self._update_wage)

        delete_button = QPushButton(self)
        delete_button.setText(strs.DELETE_BTN)
        delete_button.clicked.connect(self._delete_wage)

        print_button = QPushButton(self)
        print_button.setText(strs.PRINT_BTN)
        print_button.clicked.connect(self._print_wage)

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
        values = [self.employee_box.currentText()]

        self._wages = self._manager.actions(Actions.employee_wage, values)

        if self._wages is None:
            self.table.clearContents()
            self.table.setRowCount(0)
        else:
            self._wages = [self._wages]
            self.table.setRowCount(len(self._wages))

            # Data rows
            for row, wage in enumerate(self._wages):
                self.table.setItem(row, 0, QTableWidgetItem(str(wage.get_day())))
                self.table.setItem(row, 1, QTableWidgetItem(str(wage.get_hour())))
                self.table.setItem(row, 2, QTableWidgetItem(str(wage.get_meal())))

    def _update_wage(self):
        row_index = self._check_selection()

        if row_index is not None:
            wage = self._wages[row_index]
            values = [wage.get_wage_id(), wage.get_employee_id(), wage.get_day(), wage.get_hour(), wage.get_meal()]

            dialog = UpdateWageRowDialog(values)
            if dialog.exec():
                new_values = dialog.get_value()

                response = self._manager.actions(Actions.update_wage, new_values)

                if response == Responses.success:
                    QMessageBox.information(self, strs.PRESENT_MSG, strs.WAGE_UPD_SUCC_MSG)
                    self._change_label()
                else:
                    QMessageBox.warning(self, strs.PRESENT_MSG, strs.WAGE_UPD_FAIL_MSG)

    def _delete_wage(self):
        row_index = self._check_selection()

        if row_index is not None:
            dialog = DeleteRowDialog(self)

            if dialog.exec():
                wage = self._wages[row_index]
                values = [wage.get_wage_id(), wage.get_employee_id()]

                response = self._manager.actions(Actions.delete_wage, values)

                if response == Responses.success:
                    QMessageBox.information(self, strs.PRESENT_MSG, strs.WAGE_DEL_SUCC_MSG)
                    self._change_label()
                else:
                    QMessageBox.warning(self, strs.PRESENT_MSG, strs.WAGE_DEL_FAIL_MSG)

    def _print_wage(self):
        QMessageBox.warning(self, strs.PRESENT_MSG, strs.NOT_IMPLEMENTED_MSG)

    def _check_selection(self):
        selected_ranges = self.table.selectedRanges()

        if len(self.table.selectedItems()) != 3 or len(selected_ranges) != 1 or selected_ranges[0].rowCount() != 1:
            QMessageBox.warning(self, strs.PRESENT_MSG, strs.MUST_SELECT_ONE_ROW_MSG)
            self.table.clearSelection()

            return None

        return selected_ranges[0].topRow()

    def get_name(self):
        return self._name



