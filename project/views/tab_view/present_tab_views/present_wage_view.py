from project.views.tab_view.present_tab_views.present_view import PresentView
from project.views.tab_view.present_tab_views.present_dialogs import *
from project.utils.enums import Actions, ResponseStatus
from project.utils import strings as strs, funcs
from project.models.my_widgets import *


class PresentWageView(PresentView):

    def __init__(self, name, manager, *args, **kwargs):
        super(PresentWageView, self).__init__(*args, **kwargs)
        self._name = name
        self._manager = manager

        self._wages = None

        self._init_ui()

    def _init_ui(self):
        employee_label = MyLabel(strs.EMPLOYEE)
        self.employee_box = MyComboBox(self._generate_items())
        self.employee_box.currentTextChanged.connect(self._change_label)
        employee_label.setBuddy(self.employee_box)

        fields_layout = QFormLayout()
        fields_layout.addRow(employee_label, self.employee_box)

        self.table = MyTable(strs.PRESENT_WAGE_HDR)
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
        # Get data
        values = [self.employee_box.currentText()]

        response = self._manager.actions(Actions.employee_wage, values)
        self._wages = response.get_data()

        if self._wages is None:
            self.table.clearContents()
            self.table.setRowCount(0)
        else:
            self.table.setRowCount(len(self._wages))

            for row, wage in enumerate(self._wages):
                self.table.setItem(row, 0, QTableWidgetItem(wage.get_employee_name()))
                self.table.setItem(row, 1, QTableWidgetItem(str(wage.get_day())))
                self.table.setItem(row, 2, QTableWidgetItem(str(wage.get_hour())))
                self.table.setItem(row, 3, QTableWidgetItem(str(wage.get_meal())))

    def update(self):
        self.employee_box.update_items(self._generate_items())

        self._change_label()

    def _update(self):
        row_index = self._check_selection()

        if row_index is not None:
            wage = self._wages[row_index]
            values = wage.data_to_array()

            dialog = UpdateWageRowDialog(values)
            if dialog.exec():
                new_values = dialog.get_value()

                response = self._manager.actions(Actions.update_wage, new_values)

                funcs.show_message(self, response.get_status(), strs.PRESENT_VIEW_MSG, response.get_message())

                if response.get_status() == ResponseStatus.success:
                    self._change_label()

    def _delete(self):
        row_index = self._check_selection()

        if row_index is not None:
            dialog = DeleteRowDialog(self)

            if dialog.exec():
                wage = self._wages[row_index]
                values = [wage.get_wage_id()]

                response = self._manager.actions(Actions.delete_wage, values)

                funcs.show_message(self, response.get_status(), strs.PRESENT_VIEW_MSG, response.get_message())

                if response.get_status() == ResponseStatus.success:
                    self._change_label()

    def _print(self):
        QMessageBox.warning(self, strs.PRESENT_VIEW_MSG, strs.NOT_IMPLEMENTED_MSG)

    def _check_selection(self):
        selected_ranges = self.table.selectedRanges()

        if len(self.table.selectedItems()) != 4 or len(selected_ranges) != 1 or selected_ranges[0].rowCount() != 1:
            QMessageBox.warning(self, strs.PRESENT_VIEW_MSG, strs.MUST_SELECT_ONE_ROW_MSG)
            self.table.clearSelection()

            return None

        return selected_ranges[0].topRow()

    def get_name(self):
        return self._name



