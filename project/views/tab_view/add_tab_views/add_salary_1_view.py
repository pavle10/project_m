from project.utils import funcs as funcs, strings as strs
from project.views.tab_view.add_tab_views.add_view import AddView
from project.utils.enums import Actions, ResponseStatus
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
        values = [self.employee_box.currentText(), self.net_line.text(),
                  self.gross_line.text(), self.date_line.date().toPyDate()]

        response = self._manager.actions(Actions.add_salary_1, values)

        funcs.show_message(self, response.get_status(), strs.ADD_VIEW_MSG, response.get_message())

        if response.get_status() == ResponseStatus.success:
            self._clear()

    def _clear(self):
        self.employee_box.setCurrentIndex(0)
        self.net_line.clear()
        self.gross_line.clear()
        self.date_line.setDate(cons.DEFAULT_END_DATE)

    def get_name(self):
        return self._name
