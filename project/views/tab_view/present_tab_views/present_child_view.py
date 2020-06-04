from PyQt5.QtPrintSupport import QPrinter, QPrintPreviewDialog
from PyQt5.QtCore import QFileInfo

from project.views.tab_view.present_tab_views.present_view import PresentView
from project.views.tab_view.present_tab_views.present_dialogs import *
from project.utils.enums import Actions, ResponseStatus
from project.models.my_widgets import *
from project.utils import strings as strs


class PresentChildView(PresentView):

    def __init__(self, name, manager, *args, **kwargs):
        super(PresentChildView, self).__init__(*args, **kwargs)
        self._name = name
        self._manager = manager
        self._content = QTextEdit(self)
        self._content.hide()

        self._printer = QPrinter(QPrinter.HighResolution)
        self._printer.setFullPage(True)
        self._printer.setPageMargins(2, 5, 2, 5, QPrinter.Millimeter)

        self._init_ui()

    def _init_ui(self):
        self.table = MyTable(strs.PRESENT_CHILD_HDR)
        self._update_table()

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
        layout.addWidget(self.scroll_area)
        layout.addLayout(buttons_layout)
        self.setLayout(layout)

    def _update_table(self):
        self._children = self._manager.actions(Actions.all_children)

        self.table.setRowCount(len(self._children))

        for row, child in enumerate(self._children):
            self.table.setItem(row, 0, QTableWidgetItem(child.get_first_name()))
            self.table.setItem(row, 1, QTableWidgetItem(child.get_last_name()))
            self.table.setItem(row, 2, QTableWidgetItem(child.get_identity_number()))
            self.table.setItem(row, 3, QTableWidgetItem(str(child.get_birthday())))
            self.table.setItem(row, 4, QTableWidgetItem(child.get_mother_name()))
            self.table.setItem(row, 5, QTableWidgetItem(child.get_father_name()))

    def update(self):
        self._update_table()

    def _update(self):
        row_index = self._check_selection()

        if row_index is not None:
            child = self._children[row_index]
            values = child.data_to_array()
            employees = self._manager.actions(Actions.all_employees)

            dialog = UpdateChildDialog(values, employees)

            if dialog.exec():
                response = self._manager.actions(Actions.update_child, dialog.get_value())

                funcs.show_message(self, response.get_status(), strs.PRESENT_VIEW_MSG, response.get_message())

                if response.get_status() == ResponseStatus.success:
                    self._update_table()

    def _delete(self):
        row_index = self._check_selection()

        if row_index is not None:
            dialog = DeleteRowDialog(self)

            if dialog.exec():
                response = self._manager.actions(Actions.delete_child, [self._children[row_index].get_child_id()])

                funcs.show_message(self, response.get_status(), strs.PRESENT_VIEW_MSG, response.get_message())

                if response.get_status() == ResponseStatus.success:
                    self._update_table()

    def _print(self):
        preview_dialog = QPrintPreviewDialog(self._printer, self)

        preview_dialog.setMinimumSize(cons.PRINT_PREVIEW_DIALOG_WIDTH, cons.PRINT_PREVIEW_DIALOG_HEIGHT)
        preview_dialog.paintRequested.connect(self._print_preview)
        preview_dialog.exec_()

    def _print_preview(self):
        data = self._prepare_data()
        self._printer.setOutputFormat(QPrinter.NativeFormat)

        self._content.clear()
        self._content.insertHtml(funcs.create_html(strs.CHILDREN_LIST_TITLE, data, True, strs.PRESENT_CHILD_HDR))
        self._content.document().print_(self._printer)

    def _export_pdf(self):
        data = self._prepare_data()
        self._printer.setOutputFormat(QPrinter.PdfFormat)
        fn, _ = QFileDialog.getSaveFileName(self, strs.EXPORT_CAPTION, cons.EXPORT_DEFAULT_PATH, strs.SAVE_FILE_FILTER)

        if fn != "":
            fn = fn + ".pdf" if QFileInfo(fn).suffix() == "" else fn

            self._printer.setOutputFileName(fn)

            self._content.clear()
            self._content.insertHtml(funcs.create_html(strs.CHILDREN_LIST_TITLE, data, True, strs.PRESENT_CHILD_HDR))
            self._content.document().print_(self._printer)

    def _check_selection(self):
        selected_ranges = self.table.selectedRanges()

        if len(self.table.selectedItems()) != 6 or len(selected_ranges) != 1 or selected_ranges[0].rowCount() != 1:
            QMessageBox.warning(self, strs.PRESENT_VIEW_MSG, strs.MUST_SELECT_ONE_ROW_MSG)
            self.table.clearSelection()

            return None

        return selected_ranges[0].topRow()

    def _prepare_data(self):
        data = [child.data_for_report() for child in self._children]

        for entry in data:
            for ind in range(len(entry)):
                if entry[ind] is None:
                    entry[ind] = ""

        return data

    def get_name(self):
        return self._name
