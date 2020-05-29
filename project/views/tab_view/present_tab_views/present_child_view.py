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

        self._init_ui()

    def _init_ui(self):
        self.table = MyTable(strs.PRESENT_CHILD_HDR)
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
        self._children = self._manager.actions(Actions.all_children)

        self.table.setRowCount(len(self._children))

        for row, child in enumerate(self._children):
            self.table.setItem(row, 0, QTableWidgetItem(child.get_first_name()))
            self.table.setItem(row, 1, QTableWidgetItem(child.get_last_name()))
            self.table.setItem(row, 2, QTableWidgetItem(child.get_identity_number()))
            self.table.setItem(row, 3, QTableWidgetItem(str(child.get_birthday())))
            self.table.setItem(row, 4, QTableWidgetItem(child.get_mother_name()))
            self.table.setItem(row, 5, QTableWidgetItem(child.get_father_name()))

    def _update(self):
        row_index = self._check_selection()

        if row_index is not None:
            child = self._children[row_index]
            values = [child.get_child_id(), child.get_identity_number(), child.get_birth_year(),
                      child.get_mother_id(), child.get_mother_name(), child.get_father_id(), child.get_father_name()]
            employees = self._manager.actions(Actions.all_employees)

            dialog = UpdateChildDialog(values, employees)

            if dialog.exec():
                new_values = dialog.get_value()
                new_values = list(map(lambda x: None if x == "" else x, new_values))
                new_values[2] = int(new_values[2])

                response = self._manager.actions(Actions.update_child, new_values)

                if response == ResponseStatus.success:
                    QMessageBox.information(self, strs.PRESENT_VIEW_MSG, strs.CHILD_UPD_SUCC_MSG)
                    self.update_table()
                else:
                    QMessageBox.warning(self, strs.PRESENT_VIEW_MSG, strs.CHILD_UPD_FAIL_MSG)

    def _delete(self):
        row_index = self._check_selection()

        if row_index is not None:
            dialog = DeleteRowDialog(self)

            if dialog.exec():
                values = [self._children[row_index].get_child_id()]

                response = self._manager.actions(Actions.delete_child, values)

                if response == ResponseStatus.success:
                    QMessageBox.information(self, strs.PRESENT_VIEW_MSG, strs.CHILD_DEL_SUCC_MSG)
                    self.update_table()
                else:
                    QMessageBox.warning(self, strs.PRESENT_VIEW_MSG, strs.CHILD_DEL_FAIL_MSG)

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