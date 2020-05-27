from PyQt5.QtCore import Qt

from project.views.tab_view.present_tab_views.present_dialogs import *
from project.utils.enums import Actions, Responses
from project.utils import strings as strs, constants as cons, funcs


class PresentSalary2View(QWidget):

    def __init__(self, name, manager, *args, **kwargs):
        super(PresentSalary2View, self).__init__(*args, **kwargs)
        self._name = name
        self._manager = manager

        self._salaries = None

        self._init_ui()

    def _init_ui(self):
        employee_label = QLabel(self)
        employee_label.setText(f"*{strs.EMPLOYEE_LBL}")
        self.employee_box = QComboBox()
        self.employee_box.insertItem(0, strs.EMPTY)
        for index, employee in enumerate(self._get_employees()):
            self.employee_box.insertItem(index+1, funcs.employee_unique_name(employee))
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
        self.table.setColumnCount(len(strs.PRESENT_SALARY_2_HDR))
        self.table.setHorizontalHeaderLabels(strs.PRESENT_SALARY_2_HDR)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidget(self.table)

        update_button = QPushButton(self)
        update_button.setText(strs.UPDATE_BTN)
        update_button.clicked.connect(self._update_salary)

        delete_button = QPushButton(self)
        delete_button.setText(strs.DELETE_BTN)
        delete_button.clicked.connect(self._delete_salary)

        print_button = QPushButton(self)
        print_button.setText(strs.PRINT_BTN)
        print_button.clicked.connect(self._print_salary)

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
        values = [[self.employee_box.currentText()], self.start_date_line.date(), self.end_date_line.date()]

        self._salaries = self._manager.actions(Actions.employee_salaries_2, values)

        if self._salaries is None:
            self.table.clearContents()
            self.table.setRowCount(0)
        else:
            self.table.setRowCount(len(self._salaries))

            # Data rows
            for row, salary in enumerate(self._salaries):
                for column, item in enumerate(salary[2:]):
                    if column == 0:
                        date = item.strftime(cons.DATE_FORMAT_PYTHON)
                        self.table.setItem(row, column, QTableWidgetItem(date))
                    else:
                        self.table.setItem(row, column, QTableWidgetItem(str(item)))

    def keyReleaseEvent(self, event):

        if event.key() in [Qt.Key_Enter, Qt.Key_Return] and isinstance(self.focusWidget(), QDateEdit):
            self._change_label()

    def _update_salary(self):
        row_index = self._check_selection()

        if row_index is not None:
            values = self._salaries[row_index]

            dialog = UpdateSalary1RowDialog(values)
            if dialog.exec():
                new_values = dialog.get_value()

                response = self._manager.actions(Actions.update_salary_2, new_values)

                if response == Responses.success:
                    QMessageBox.information(self, strs.PRESENT_VIEW_MSG, strs.SALARY_2_UPD_SUCC_MSG)
                    self._change_label()
                else:
                    QMessageBox.warning(self, strs.PRESENT_VIEW_MSG, strs.SALARY_2_UPD_FAIL_MSG)

    def _delete_salary(self):
        row_index = self._check_selection()

        if row_index is not None:
            dialog = DeleteRowDialog(self)

            if dialog.exec():
                values = [self._salaries[row_index][0]]

                response = self._manager.actions(Actions.delete_salary_2, values)

                if response == Responses.success:
                    QMessageBox.information(self, strs.PRESENT_VIEW_MSG, strs.SALARY_2_DEL_SUCC_MSG)
                    self._change_label()
                else:
                    QMessageBox.warning(self, strs.PRESENT_VIEW_MSG, strs.SALARY_2_DEL_FAIL_MSG)

    def _print_salary(self):
        QMessageBox.warning(self, strs.PRESENT_VIEW_MSG, strs.NOT_IMPLEMENTED_MSG)

    def _check_selection(self):
        selected_ranges = self.table.selectedRanges()

        if len(self.table.selectedItems()) != 11 or len(selected_ranges) != 1 or selected_ranges[0].rowCount() != 1:
            QMessageBox.warning(self, strs.PRESENT_VIEW_MSG, strs.MUST_SELECT_ONE_ROW_MSG)
            self.table.clearSelection()

            return None

        return selected_ranges[0].topRow()

    def get_name(self):
        return self._name
