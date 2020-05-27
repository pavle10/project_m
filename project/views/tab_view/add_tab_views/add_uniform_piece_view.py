from project.utils import funcs as funcs, strings as strs
from project.views.add_tab_views.add_view import AddView
from project.utils.enums import Actions, Responses
from project.models.my_widgets import *


class AddUniformPieceView(AddView):

    def __init__(self, name, manager, *args, **kwargs):
        super(AddUniformPieceView, self).__init__(*args, **kwargs)
        self._name = name
        self._manager = manager

        self._init_ui()

    def _init_ui(self):
        uniform_label = MyLabel(strs.UNIFORM, is_required=True)
        self.uniform_box = MyComboBox()
        for index, uniform in enumerate(self._get_uniforms()):
            self.uniform_box.insertItem(index, f"{uniform.get_name()}")
        uniform_label.setBuddy(self.uniform_box)

        employee_label = MyLabel(strs.EMPLOYEE, is_required=True)
        self.employee_box = MyComboBox()
        for index, employee in enumerate(self._get_employees()):
            self.employee_box.insertItem(index, funcs.employee_unique_name(employee))
        employee_label.setBuddy(self.employee_box)

        size_label = MyLabel(strs.PRESENT_UNIFORM_PIECE_HDR[1], is_required=True)
        self.size_line = MyEditLine()
        size_label.setBuddy(self.size_line)

        quantity_label = MyLabel(strs.PRESENT_UNIFORM_PIECE_HDR[2], is_required=True)
        self.quantity_line = MyEditLine()
        quantity_label.setBuddy(self.quantity_line)

        additional_label = MyLabel(strs.PRESENT_UNIFORM_PIECE_HDR[3])
        self.additional_line = MyEditLine()
        additional_label.setBuddy(self.additional_line)

        date_label = MyLabel(strs.PRESENT_UNIFORM_PIECE_HDR[4], is_required=True)
        self.date_line = MyEditDate()
        date_label.setBuddy(self.date_line)

        add_button = MyButton(strs.ADD_BTN)
        add_button.clicked.connect(self._add)

        layout = QFormLayout()
        layout.addRow(uniform_label, self.uniform_box)
        layout.addRow(employee_label, self.employee_box)
        layout.addRow(size_label, self.size_line)
        layout.addRow(quantity_label, self.quantity_line)
        layout.addRow(additional_label, self.additional_line)
        layout.addRow(date_label, self.date_line)
        layout.addWidget(add_button)
        self.setLayout(layout)

    def _get_uniforms(self):
        return self._manager.actions(Actions.all_uniforms)

    def _get_employees(self):
        return self._manager.actions(Actions.all_employees)

    def _add(self):
        chosen_date = self.date_line.date().toPyDate()
        values = [self.uniform_box.currentText(), self.employee_box.currentText(), self.size_line.text(),
                  self.quantity_line.text(), self.additional_line.text(), chosen_date]

        response = self._manager.actions(Actions.add_uniform_piece, values)

        if response == Responses.success:
            QMessageBox.information(self, strs.ADD_VIEW_MSG, strs.UNIFORM_PIECE_ADD_SUCC_MSG)
        elif response == Responses.fail:
            QMessageBox.warning(self, strs.ADD_VIEW_MSG, strs.UNIFORM_PIECE_ADD_FAIL_MSG)

    def get_name(self):
        return self._name
