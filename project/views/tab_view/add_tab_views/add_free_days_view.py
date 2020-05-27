from project.views.add_tab_views.add_view import AddView
from project.models.my_widgets import *
from project.utils.enums import Actions, Responses
from project.utils import funcs as funcs, strings as strs


class AddFreeDaysView(AddView):

    def __init__(self, name, manager, *args, **kwargs):
        super(AddFreeDaysView, self).__init__(*args, **kwargs)
        self._name = name
        self._manager = manager

        self._init_ui()

    def _init_ui(self):
        employee_label = MyLabel(strs.EMPLOYEE, is_required=True)
        self.employee_box = MyComboBox()
        for index, employee in enumerate(self._get_employees()):
            self.employee_box.insertItem(index, funcs.employee_unique_name(employee))
        employee_label.setBuddy(self.employee_box)

        reason_label = MyLabel(strs.PRESENT_FREE_DAYS_HDR[3])
        self.reason_line = MyEditLine()
        reason_label.setBuddy(self.reason_line)

        start_date_label = MyLabel(strs.PRESENT_FREE_DAYS_HDR[0], is_required=True)
        self.start_date_line = MyEditDate(cons.DEFAULT_START_DATE)
        start_date_label.setBuddy(self.start_date_line)

        end_date_label = MyLabel(strs.PRESENT_FREE_DAYS_HDR[1], is_required=True)
        self.end_date_line = MyEditDate()
        end_date_label.setBuddy(self.end_date_line)

        add_button = MyButton(strs.ADD_BTN)
        add_button.clicked.connect(self._add)

        layout = QFormLayout()
        layout.addRow(employee_label, self.employee_box)
        layout.addRow(reason_label, self.reason_line)
        layout.addRow(start_date_label, self.start_date_line)
        layout.addRow(end_date_label, self.end_date_line)
        layout.addWidget(add_button)
        self.setLayout(layout)

    def _get_employees(self):
        return self._manager.actions(Actions.all_employees)

    def _add(self):
        start_date = self.start_date_line.date().toPyDate()
        end_date = self.end_date_line.date().toPyDate()
        # TODO implement valid total days calculation and move it to controller
        total_days = end_date - start_date

        values = [self.employee_box.currentText(), start_date, end_date, total_days.days,  self.reason_line.text()]

        response = self._manager.actions(Actions.add_free_days, values)

        if response == Responses.success:
            QMessageBox.information(self, strs.ADD_VIEW_MSG, strs.FREE_DAYS_ADD_SUCC_MSG)
        elif response == Responses.fail:
            QMessageBox.warning(self, strs.ADD_VIEW_MSG, strs.FREE_DAYS_ADD_FAIL_MSG)

    def get_name(self):
        return self._name

