from project.views.tab_view.add_tab_views.add_view import AddView
from project.utils.enums import Actions, ResponseStatus
from project.utils import strings as strs, funcs
from project.models.my_widgets import *


class AddChildView(AddView):

    def __init__(self, name, manager, *args, **kwargs):
        super(AddChildView, self).__init__(*args, **kwargs)
        self._name = name
        self._manager = manager

        self._init_ui()

    def _init_ui(self):
        first_name_label = MyLabel(strs.PRESENT_CHILD_HDR[0], is_required=True)
        self.first_name_line = MyEditLine()
        first_name_label.setBuddy(self.first_name_line)

        last_name_label = MyLabel(strs.PRESENT_CHILD_HDR[1], is_required=True)
        self.last_name_line = MyEditLine()
        last_name_label.setBuddy(self.last_name_line)

        identity_number_label = MyLabel(strs.PRESENT_CHILD_HDR[2])
        self.identity_number_line = MyEditLine()
        identity_number_label.setBuddy(self.identity_number_line)

        birthday_label = MyLabel(strs.PRESENT_CHILD_HDR[3], is_required=True)
        self.birthday_line = MyEditDate()
        birthday_label.setBuddy(self.birthday_line)

        mother_label = MyLabel(strs.PRESENT_CHILD_HDR[4])
        # TODO Think about better MyComboBox initialization
        self.mother_box = MyComboBox()
        self.mother_box.insertItem(0, strs.EMPTY)
        for index, employee in enumerate(self._get_employees()):
            self.mother_box.insertItem(index+1, funcs.employee_unique_name(employee))
        mother_label.setBuddy(self.mother_box)

        father_label = MyLabel(strs.PRESENT_CHILD_HDR[5])
        self.father_box = MyComboBox()
        self.father_box.insertItem(0, strs.EMPTY)
        for index, employee in enumerate(self._get_employees()):
            self.father_box.insertItem(index+1, funcs.employee_unique_name(employee))
        father_label.setBuddy(self.father_box)

        add_button = MyButton(strs.ADD_BTN)
        add_button.clicked.connect(self._add)

        layout = QFormLayout()
        layout.addRow(first_name_label, self.first_name_line)
        layout.addRow(last_name_label, self.last_name_line)
        layout.addRow(identity_number_label, self.identity_number_line)
        layout.addRow(birthday_label, self.birthday_line)
        layout.addRow(mother_label, self.mother_box)
        layout.addRow(father_label, self.father_box)
        layout.addWidget(add_button)
        self.setLayout(layout)

    def _get_employees(self):
        return self._manager.actions(Actions.all_employees)

    def _add(self):
        values = [self.first_name_line.text(), self.last_name_line.text(), self.identity_number_line.text(),
                  self.birthday_line.date().toPyDate(), self.mother_box.currentText(), self.father_box.currentText()]

        response = self._manager.actions(Actions.add_child, values)

        funcs.show_message(self, response.get_status(), strs.ADD_VIEW_MSG, response.get_message())

        if response.get_status() == ResponseStatus.success:
            self._clear()

    def _clear(self):
        self.first_name_line.clear()
        self.last_name_line.clear()
        self.identity_number_line.clear()
        self.birthday_line.setDate(cons.DEFAULT_END_DATE)
        self.mother_box.setCurrentIndex(0)
        self.father_box.setCurrentIndex(0)

    def get_name(self):
        return self._name

