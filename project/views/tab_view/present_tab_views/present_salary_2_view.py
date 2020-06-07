from PyQt5.QtPrintSupport import QPrinter, QPrintPreviewDialog
from PyQt5.QtCore import QFileInfo
from PyQt5.QtCore import Qt

from project.views.tab_view.present_tab_views.present_view import PresentView
from project.views.tab_view.present_tab_views.present_dialogs import *
from project.utils.enums import Actions, ResponseStatus
from project.utils import strings as strs, funcs
from project.models.my_widgets import *


class PresentSalary2View(PresentView):

    def __init__(self, name, manager, *args, **kwargs):
        super(PresentSalary2View, self).__init__(*args, **kwargs)
        self._name = name
        self._manager = manager
        self._content = QTextEdit(self)
        self._content.hide()

        self._printer = QPrinter(QPrinter.HighResolution)
        self._printer.setFullPage(True)
        self._printer.setPageMargins(2, 5, 2, 5, QPrinter.Millimeter)
        self._printer.setOrientation(QPrinter.Landscape)

        self._salaries = None

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

        self.table = MyTable(strs.PRESENT_SALARY_2_HDR)
        self._change_label()

        # TODO make my_widget class for scroll area
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.table)

        update_button = MyButton(strs.UPDATE_BTN)
        update_button.clicked.connect(self._update)

        delete_button = MyButton(strs.DELETE_BTN)
        delete_button.clicked.connect(self._delete)

        print_button = MyButton(strs.PRINT_BTN)
        print_button.clicked.connect(self._print)

        export_button = MyButton(strs.EXPORT_BTN)
        export_button.clicked.connect(self._export_pdf)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(update_button)
        buttons_layout.addWidget(delete_button)
        buttons_layout.addWidget(print_button)
        buttons_layout.addWidget(export_button)

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
        values = [self.employee_box.currentText(),
                  self.start_date_line.date().toPyDate(),
                  self.end_date_line.date().toPyDate()]

        response = self._manager.actions(Actions.employee_salaries_2, values)
        self._salaries = response.get_data()

        if response.get_status() == ResponseStatus.fail:
            funcs.show_message(self, response.get_status(), strs.PRESENT_VIEW_MSG, response.get_message())
            self.table.clearContents()
            self.table.setRowCount(0)
        else:
            self.table.empty_data()
            self.table.setRowCount(len(self._salaries))

            # Data rows
            for row, salary in enumerate(self._salaries):
                row_data = [salary[2].strftime(cons.DATE_FORMAT_PYTHON), salary[-1], str(salary[3]), str(salary[4]),
                            str(salary[5]), str(salary[6]), str(salary[7]), str(salary[8]), str(salary[9]),
                            str(salary[10]), str(salary[11]), str(salary[12])]

                self.table.add_row(row, row_data)

    def update(self):
        self.employee_box.update_items(self._generate_items())

        self._change_label()

    def keyReleaseEvent(self, event):

        if event.key() in [Qt.Key_Enter, Qt.Key_Return] and isinstance(self.focusWidget(), QDateEdit):
            self._change_label()

    def _update(self):
        row_index = self._check_selection()

        if row_index is not None:
            values = self._salaries[row_index]

            dialog = UpdateSalary2RowDialog(values[:-1])
            if dialog.exec():
                new_values = dialog.get_value()

                response = self._manager.actions(Actions.update_salary_2, new_values)

                funcs.show_message(self, response.get_status(), strs.PRESENT_VIEW_MSG, response.get_message())

                if response.get_status() == ResponseStatus.success:
                    self._change_label()

    def _delete(self):
        row_index = self._check_selection()

        if row_index is not None:
            dialog = DeleteRowDialog(self)

            if dialog.exec():
                values = [self._salaries[row_index][0]]

                response = self._manager.actions(Actions.delete_salary_2, values)

                funcs.show_message(self, response.get_status(), strs.PRESENT_VIEW_MSG, response.get_message())

                if response.get_status() == ResponseStatus.success:
                    self._change_label()

    def _print(self):
        preview_dialog = QPrintPreviewDialog(self._printer, self)

        preview_dialog.setMinimumSize(cons.PRINT_PREVIEW_DIALOG_WIDTH, cons.PRINT_PREVIEW_DIALOG_HEIGHT)
        preview_dialog.paintRequested.connect(self._print_preview)
        preview_dialog.exec_()

    def _print_preview(self):
        data = self._prepare_data()
        self._printer.setOutputFormat(QPrinter.NativeFormat)

        self._content.clear()
        self._content.insertHtml(funcs.create_html(strs.SALARY_2_LIST_TITLE, data,
                                                   strs.PRESENT_SALARY_2_HDR, strs.SALARY_2))
        self._content.document().print_(self._printer)

    def _export_pdf(self):
        data = self._prepare_data()
        self._printer.setOutputFormat(QPrinter.PdfFormat)
        fn, _ = QFileDialog.getSaveFileName(self, strs.EXPORT_CAPTION, cons.EXPORT_DEFAULT_PATH, strs.SAVE_FILE_FILTER)

        if fn != "":
            fn = fn + ".pdf" if QFileInfo(fn).suffix() == "" else fn

            self._printer.setOutputFileName(fn)

            self._content.clear()
            self._content.insertHtml(funcs.create_html(strs.SALARY_2_LIST_TITLE, data,
                                                       strs.PRESENT_SALARY_2_HDR, strs.SALARY_2))
            self._content.document().print_(self._printer)

    def _check_selection(self):
        selected_ranges = self.table.selectedRanges()

        if len(self.table.selectedItems()) != 12 or len(selected_ranges) != 1 or selected_ranges[0].rowCount() != 1:
            QMessageBox.warning(self, strs.PRESENT_VIEW_MSG, strs.MUST_SELECT_ONE_ROW_MSG)
            self.table.clearSelection()

            return None

        return selected_ranges[0].topRow()

    def _prepare_data(self):
        table_data = self.table.get_data()
        data = dict()

        data["dates"] = [[self.start_date_line.date().toPyDate().strftime(cons.DATE_FORMAT_PYTHON),
                          self.end_date_line.date().toPyDate().strftime(cons.DATE_FORMAT_PYTHON)]]

        for index, row in enumerate(table_data):
            date = row[0]
            employee = row[1]

            funcs.convert_to_int(row, [2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

            day_pay = row[2] * row[3]
            hour_pay = row[4] * row[5]
            meal_pay = row[6] * row[7]
            vacation_pay = row[9] * row[10] * (-1)
            rate_pay = row[8] * (-1)
            fix_pay = row[11]
            overall_pay = day_pay + hour_pay + meal_pay + vacation_pay + rate_pay + fix_pay

            day = ("Dan", str(row[2]), str(row[3]), str(day_pay))
            hour = ("Sat", str(row[4]), str(row[5]), str(hour_pay))
            meal = ("Obrok", str(row[6]), str(row[7]), str(meal_pay))
            vacation = ("Odmor", str(row[9]), str(row[10]), str(vacation_pay))
            rate = ("Rate", "", "", str(rate_pay))
            fix = ("Fiksno", "", "", str(fix_pay))
            overall = ("Ukupno", "", "", str(overall_pay))

            data[index] = [date, employee, day, hour, meal, vacation, rate, fix, overall]

        return data

    def get_name(self):
        return self._name
