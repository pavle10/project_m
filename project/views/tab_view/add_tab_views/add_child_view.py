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
        identity_number_label = MyLabel(strs.PRESENT_CHILD_HDR[0])
        self.identity_number_line = MyEditLine(self)
        identity_number_label.setBuddy(self.identity_number_line)

        birth_year_label = MyLabel(strs.PRESENT_CHILD_HDR[1], is_required=True)
        self.birth_year_line = MyEditLine(self)
        birth_year_label.setBuddy(self.birth_year_line)

        mother_label = MyLabel(strs.PRESENT_CHILD_HDR[2])
        # TODO Think about better MyComboBox initialization
        self.mother_box = MyComboBox()
        self.mother_box.insertItem(0, strs.EMPTY)
        for index, employee in enumerate(self._get_employees()):
            self.mother_box.insertItem(index+1, funcs.employee_unique_name(employee))
        mother_label.setBuddy(self.mother_box)

        father_label = MyLabel(strs.PRESENT_CHILD_HDR[3])
        self.father_box = MyComboBox()
        self.father_box.insertItem(0, strs.EMPTY)
        for index, employee in enumerate(self._get_employees()):
            self.father_box.insertItem(index+1, funcs.employee_unique_name(employee))
        father_label.setBuddy(self.father_box)

        add_button = MyButton(strs.ADD_BTN)
        add_button.clicked.connect(self._add)

        layout = QFormLayout()
        layout.addRow(identity_number_label, self.identity_number_line)
        layout.addRow(birth_year_label, self.birth_year_line)
        layout.addRow(mother_label, self.mother_box)
        layout.addRow(father_label, self.father_box)
        layout.addWidget(add_button)
        self.setLayout(layout)

    def _get_employees(self):
        return self._manager.actions(Actions.all_employees)

    def _add(self):
        mother = self.mother_box.currentText()
        father = self.father_box.currentText()

        if mother == strs.EMPTY and father == strs.EMPTY:
            QMessageBox.warning(self, strs.ADD_VIEW_MSG, strs.CHILD_ONE_PARENT_REQUIRED)

            return

        values = [self.identity_number_line.text(), self.birth_year_line.text(), mother, father]

        response = self._manager.actions(Actions.add_child, values)

        if response == ResponseStatus.success:
            QMessageBox.information(self, strs.ADD_VIEW_MSG, strs.CHILD_ADD_SUCC_MSG)
        elif response == ResponseStatus.fail:
            QMessageBox.warning(self, strs.ADD_VIEW_MSG, strs.CHILD_ADD_FAIL_MSG)

    def get_name(self):
        return self._name

