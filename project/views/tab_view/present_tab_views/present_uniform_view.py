from project.views.tab_view.present_tab_views.present_view import PresentView
from project.views.tab_view.present_tab_views.present_dialogs import *
from project.utils.enums import Actions, ResponseStatus
from project.utils import strings as strs
from project.models.my_widgets import *


class PresentUniformView(PresentView):

    def __init__(self, name, manager, *args, **kwargs):
        super(PresentUniformView, self).__init__(*args, **kwargs)
        self._name = name
        self._manager = manager

        self._init_ui()

    def _init_ui(self):
        self.table = MyTable(strs.PRESENT_UNIFORM_HDR)
        self.update_table()

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
        layout.addWidget(self.scroll_area)
        layout.addLayout(buttons_layout)
        self.setLayout(layout)

    def update_table(self):
        uniforms = self._manager.actions(Actions.all_uniforms)

        self.table.setRowCount(len(uniforms))

        for row, uniform in enumerate(uniforms):
            self.table.setItem(row, 0, QTableWidgetItem(uniform.get_name()))

    def _update(self):
        row_index = self._check_selection()

        if row_index is not None:
            values = [self.table.currentItem().text(), ""]

            dialog = UpdateUniformDialog(values)

            if dialog.exec():
                new_values = dialog.get_value()

                response = self._manager.actions(Actions.update_uniform, new_values)

                funcs.show_message(self, response.get_status(), strs.PRESENT_VIEW_MSG, response.get_message())

                if response.get_status() == ResponseStatus.success:
                    self.update_table()

    def _delete(self):
        row_index = self._check_selection()

        if row_index is not None:
            dialog = DeleteRowDialog(self)

            if dialog.exec():
                values = [self.table.currentItem().text()]

                response = self._manager.actions(Actions.delete_uniform, values)

                funcs.show_message(self, response.get_status(), strs.PRESENT_VIEW_MSG, response.get_message())

                if response.get_status() == ResponseStatus.success:
                    self.update_table()

    def _print(self):
        QMessageBox.warning(self, strs.PRESENT_VIEW_MSG, strs.NOT_IMPLEMENTED_MSG)

    def _check_selection(self):
        selected_ranges = self.table.selectedRanges()

        if len(self.table.selectedItems()) != 1 or len(selected_ranges) != 1 or selected_ranges[0].rowCount() != 1:
            QMessageBox.warning(self, strs.PRESENT_VIEW_MSG, strs.MUST_SELECT_ONE_ROW_MSG)
            self.table.clearSelection()

            return None

        return selected_ranges[0].topRow()

    def get_name(self):
        return self._name
