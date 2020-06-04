from PyQt5.QtPrintSupport import QPrinter, QPrintPreviewDialog
from PyQt5.QtCore import QFileInfo
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
        self._content = QTextEdit(self)
        self._content.hide()

        self._printer = QPrinter(QPrinter.HighResolution)
        self._printer.setFullPage(True)
        self._printer.setPageMargins(2, 5, 2, 5, QPrinter.Millimeter)
        self._printer.setOrientation(QPrinter.Landscape)

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
        values = [self.employee_box.currentText(), self.start_date_line.date(), self.end_date_line.date()]

        response = self._manager.actions(Actions.employee_free_days, values)

        self._free_days = response.get_data()

        self.table.empty_data()
        self.table.setRowCount(len(self._free_days))

        for row, free_days in enumerate(self._free_days):
            start_date = free_days.get_start_date().strftime(cons.DATE_FORMAT_PYTHON)
            end_date = free_days.get_end_date().strftime(cons.DATE_FORMAT_PYTHON)
            row_data = [free_days.get_employee_name(), start_date, end_date,
                        str(free_days.get_total_days()), free_days.get_reason()]

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
        preview_dialog = QPrintPreviewDialog(self._printer, self)

        preview_dialog.setMinimumSize(cons.PRINT_PREVIEW_DIALOG_WIDTH, cons.PRINT_PREVIEW_DIALOG_HEIGHT)
        preview_dialog.paintRequested.connect(self._print_preview)
        preview_dialog.exec_()

    def _print_preview(self):
        data = self.table.get_data()
        self._printer.setOutputFormat(QPrinter.NativeFormat)

        self._content.clear()
        self._content.insertHtml(funcs.create_html(strs.FREE_DAYS_LIST_TITLE, data, strs.PRESENT_FREE_DAYS_HDR))
        self._content.document().print_(self._printer)

    def _export_pdf(self):
        data = self.table.get_data()
        self._printer.setOutputFormat(QPrinter.PdfFormat)
        fn, _ = QFileDialog.getSaveFileName(self, strs.EXPORT_CAPTION, cons.EXPORT_DEFAULT_PATH, strs.SAVE_FILE_FILTER)

        if fn != "":
            fn = fn + ".pdf" if QFileInfo(fn).suffix() == "" else fn

            self._printer.setOutputFileName(fn)

            self._content.clear()
            self._content.insertHtml(funcs.create_html(strs.FREE_DAYS_LIST_TITLE, data, strs.PRESENT_FREE_DAYS_HDR))
            self._content.document().print_(self._printer)

    def _check_selection(self):
        selected_ranges = self.table.selectedRanges()

        if len(self.table.selectedItems()) != 5 or len(selected_ranges) != 1 or selected_ranges[0].rowCount() != 1:
            QMessageBox.warning(self, strs.PRESENT_VIEW_MSG, strs.MUST_SELECT_ONE_ROW_MSG)
            self.table.clearSelection()

            return None

        return selected_ranges[0].topRow()

    def get_name(self):
        return self._name
