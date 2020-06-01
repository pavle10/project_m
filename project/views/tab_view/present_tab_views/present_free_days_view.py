from PyQt5.QtCore import Qt

from project.views.tab_view.present_tab_views.present_view import PresentView
from project.views.tab_view.present_tab_views.present_dialogs import *
from project.utils.enums import Actions, ResponseStatus
from project.utils import strings as strs, funcs
from project.models.my_widgets import *


class PresentFreeDaysView(PresentView):

    def __init__(self, name, manager, *args, **kwargs):
        super(PresentFreeDaysView, self).__init__(*args, **kwargs)
        self._name = name
        self._manager = manager

        self._free_days = None

        self._init_ui()

    def _init_ui(self):
        employee_label = MyLabel(strs.EMPLOYEE)
        self.employee_box = MyComboBox(self._generate_items())
        self.employee_box.currentTextChanged.connect(self._change_label)
        employee_label.setBuddy(self.employee_box)

        start_date_label = MyLabel(strs.FROM_DATE_LBL)
        self.start_date_line = MyEditDate(cons.DEFAULT_START_DATE)
        start_date_label.setBuddy(self.start_date_line)

        end_date_label = MyLabel(strs.TO_DATE_LBL)
        self.end_date_line = MyEditDate()
        end_date_label.setBuddy(self.end_date_line)

        fields_layout = QFormLayout()
        fields_layout.addRow(employee_label, self.employee_box)
        fields_layout.addRow(start_date_label, self.start_date_line)
        fields_layout.addRow(end_date_label, self.end_date_line)

        self.table = MyTable(strs.PRESENT_FREE_DAYS_HDR)
        self._change_label()

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.table)

        update_button = MyButton(strs.UPDATE_BTN)
        update_button.clicked.connect(self._update)

        delete_button = MyButton(strs.DELETE_BTN)
        delete_button.clicked.connect(self._delete)

        print_button = MyButton(strs.PRINT_BTN)
        print_button.clicked.connect(self._print)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(update_button)
        buttons_layout.addWidget(delete_button)
        buttons_layout.addWidget(print_button)

        layout = QVBoxLayout()
        layout.addLayout(fields_layout)
        layout.addWidget(self.scroll_area)
        layout.addLayout(buttons_layout)
        self.setLayout(layout)

    def _generate_items(self):
        items = list()

        items.append(strs.ALL)

        for employee in self._get_employees():
            items.append(funcs.employee_unique_name(employee))

        return items

    def _get_employees(self):
        return self._manager.actions(Actions.all_employees)

    def _change_label(self):
        values = [self.employee_box.currentText(), self.start_date_line.date(), self.end_date_line.date()]

        response = self._manager.actions(Actions.employee_free_days, values)

        self._free_days = response.get_data()

        self.table.setRowCount(len(self._free_days))

        for row, free_days in enumerate(self._free_days):
            start_date = free_days.get_start_date().strftime(cons.DATE_FORMAT_PYTHON)
            end_date = free_days.get_end_date().strftime(cons.DATE_FORMAT_PYTHON)

            self.table.setItem(row, 0, QTableWidgetItem(free_days.get_employee_name()))
            self.table.setItem(row, 1, QTableWidgetItem(start_date))
            self.table.setItem(row, 2, QTableWidgetItem(end_date))
            self.table.setItem(row, 3, QTableWidgetItem(str(free_days.get_total_days())))
            self.table.setItem(row, 4, QTableWidgetItem(free_days.get_reason()))

    def update(self):
        self.employee_box.update_items(self._generate_items())

        self._change_label()

    def keyReleaseEvent(self, event):
        if event.key() in [Qt.Key_Enter, Qt.Key_Return] and isinstance(self.focusWidget(), QDateEdit):
            self._change_label()

    def _update(self):
        row_index = self._check_selection()

        if row_index is not None:
            values = self._free_days[row_index].data_to_array()

            dialog = UpdateFreeDaysRowDialog(values)
            if dialog.exec():
                new_values = dialog.get_value()

                response = self._manager.actions(Actions.update_free_days, new_values)

                funcs.show_message(self, response.get_status(), strs.PRESENT_VIEW_MSG, response.get_message())

                if response.get_status() == ResponseStatus.success:
                    self._change_label()

    def _delete(self):
        row_index = self._check_selection()

        if row_index is not None:
            dialog = DeleteRowDialog(self)

            if dialog.exec():
                values = [self._free_days[row_index].get_free_days_id()]

                response = self._manager.actions(Actions.delete_free_days, values)

                funcs.show_message(self, response.get_status(), strs.PRESENT_VIEW_MSG, response.get_message())

                if response.get_status() == ResponseStatus.success:
                    self._change_label()

    def _print(self):
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
