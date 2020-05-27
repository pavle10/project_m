from project.utils import funcs as funcs, strings as strs
from project.views.add_tab_views.add_view import AddView
from project.utils.enums import Actions, Responses
from project.models.my_widgets import *


class AddSalary1View(AddView):

    def __init__(self, name, manager, *args, **kwargs):
        super(AddSalary1View, self).__init__(*args, **kwargs)
        self._name = name
        self._manager = manager

        self._init_ui()

    def _init_ui(self):
        employee_label = MyLabel(strs.EMPLOYEE, is_required=True)
        self.employee_box = MyComboBox()
        for index, employee in enumerate(self._get_employees()):
            self.employee_box.insertItem(index, funcs.employee_unique_name(employee))
        employee_label.setBuddy(self.employee_box)

        net_label = MyLabel(strs.PRESENT_SALARY_1_HDR[0], is_required=True)
        self.net_line = MyEditLine()
        net_label.setBuddy(self.net_line)

        gross_label = MyLabel(strs.PRESENT_SALARY_1_HDR[1], is_required=True)
        self.gross_line = MyEditLine()
        gross_label.setBuddy(self.gross_line)

        date_label = MyLabel(strs.PRESENT_SALARY_1_HDR[2], is_required=True)
        self.date_line = MyEditDate()
        date_label.setBuddy(self.date_line)

        add_button = MyButton(strs.ADD_BTN)
        add_button.clicked.connect(self._add)

        layout = QFormLayout()
        layout.addRow(employee_label, self.employee_box)
        layout.addRow(net_label, self.net_line)
        layout.addRow(gross_label, self.gross_line)
        layout.addRow(date_label, self.date_line)
        layout.addWidget(add_button)
        self.setLayout(layout)

    def _get_employees(self):
        return self._manager.actions(Actions.all_employees)

    def _add(self):
        chosen_date = self.date_line.date().toPyDate()
        values = [self.employee_box.currentText(), self.net_line.text(), self.gross_line.text(), chosen_date]

        response = self._manager.actions(Actions.add_salary_1, values)

        if response == Responses.success:
            QMessageBox.information(self, strs.ADD_VIEW_MSG, strs.SALARY_1_ADD_SUCC_MSG)
        elif response == Responses.fail:
            QMessageBox.warning(self, strs.ADD_VIEW_MSG, strs.SALARY_1_ADD_FAIL_MSG)

    def get_name(self):
        return self._name
