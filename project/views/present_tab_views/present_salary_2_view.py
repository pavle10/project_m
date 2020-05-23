from PyQt5 import QtGui

from project.views.present_tab_views.present_dialogs import *
from project.utils.enums import Actions, Responses
from project.utils import strings as strs, constants as cons


class PresentSalary2View(QWidget):

    def __init__(self, name, manager, *args, **kwargs):
        super(PresentSalary2View, self).__init__(*args, **kwargs)
        self._name = name
        self._manager = manager

        self._salaries = None

        self._init_ui()

    def _init_ui(self):
        employee_label = QLabel(self)
        employee_label.setText("Zaposleni*:")
        self.employee_box = QComboBox()
        self.employee_box.insertItem(0, strs.EMPTY)
        for index, employee in enumerate(self._get_employees()):
            self.employee_box.insertItem(index+1, f"{employee[0]} {employee[1]} {employee[2]}")
        self.employee_box.currentTextChanged.connect(self._change_label)
        employee_label.setBuddy(self.employee_box)

        self.table = QTableWidget()
        self.table.setColumnCount(11)
        self.table.setHorizontalHeaderLabels(["Datum", "Radnih dana", "Vrednost radnog dana", "Radnih sati",
                                              "Vrednost radnog sata", "Obroka", "Vrednost obroka", "Rate",
                                              "Dana odmora", "Vrednost dana odmora", "Fiksno"])
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidget(self.table)

        update_button = QPushButton(self)
        update_button.setText("Promeni")
        update_button.clicked.connect(self._update_salary)

        delete_button = QPushButton(self)
        delete_button.setText("Obriši")
        delete_button.clicked.connect(self._delete_salary)

        print_button = QPushButton(self)
        print_button.setText("Štampaj")
        print_button.clicked.connect(self._print_salary)

        layout = QVBoxLayout()
        layout.addWidget(employee_label)
        layout.addWidget(self.employee_box)
        layout.addWidget(self.scroll_area)
        layout.addWidget(update_button)
        layout.addWidget(delete_button)
        layout.addWidget(print_button)
        self.setLayout(layout)

    def _get_employees(self):
        return self._manager.actions(Actions.all_employees)

    def _change_label(self):
        # Get data
        values = [self.employee_box.currentText()]

        self._salaries = self._manager.actions(Actions.employee_salaries_2, values)

        if self._salaries == Responses.fail:
            self.table.clear()
        else:
            self.table.setRowCount(len(self._salaries))

            # Data rows
            for row, salary in enumerate(self._salaries):
                for column, item in enumerate(salary[2:]):
                    if column == 0:
                        date = item.strftime(cons.DATE_FORMAT)
                        self.table.setItem(row, column, QTableWidgetItem(date))
                    else:
                        self.table.setItem(row, column, QTableWidgetItem(str(item)))

    def _update_salary(self):
        row_index = self._check_selection()

        if row_index:
            values = [self._salaries[row_index][0]]

            dialog = UpdateRowDialog(values)
            decision = dialog.exec()

            print(decision)

    def _delete_salary(self):
        row_index = self._check_selection()

        if row_index:
            dialog = DeleteRowDialog(self)

            if dialog.exec():
                values = [self._salaries[row_index][0]]

                response = self._manager.actions(Actions.delete_salary_2, values)

                if response == Responses.success:
                    QMessageBox.information(self, strs.PRESENT_MSG, strs.SALARY_2_DEL_SUCC_MSG)
                    self._salaries.remove(self._salaries[row_index])
                    self._change_label()
                else:
                    QMessageBox.warning(self, strs.PRESENT_MSG, strs.SALARY_2_DEL_FAIL_MSG)

    def _print_salary(self):
        QMessageBox.warning(self, strs.PRESENT_MSG, strs.NOT_IMPLEMENTED_MSG)

    def _check_selection(self):
        selected_ranges = self.table.selectedRanges()

        if len(self.table.selectedItems()) != 11 or len(selected_ranges) != 1 or selected_ranges[0].rowCount() != 1:
            QMessageBox.warning(self, strs.PRESENT_MSG, strs.MUST_SELECT_ONE_ROW_MSG)
            self.table.clearSelection()

            return None

        return selected_ranges[0].topRow()

    def get_name(self):
        return self._name
