from project.views.tab_view.add_tab_views.add_view import AddView
from project.utils.enums import Actions, ResponseStatus
from project.utils import strings as strs
from project.models.my_widgets import *


class AddPositionView(AddView):

    def __init__(self, name, manager, *args, **kwargs):
        super(AddPositionView, self).__init__(*args, **kwargs)
        self._name = name
        self._manager = manager

        self._init_ui()

    def _init_ui(self):
        name_label = MyLabel(strs.PRESENT_POSITION_HDR[0], is_required=True)
        self.name_line = MyEditLine()
        name_label.setBuddy(self.name_line)

        saturday_label = MyLabel(strs.PRESENT_POSITION_HDR[1], is_required=True)
        self.saturday = MyComboBox()
        self.saturday.addItem(strs.YES)
        self.saturday.addItem(strs.NO)
        saturday_label.setBuddy(self.saturday)

        add_button = MyButton(strs.ADD_BTN)
        add_button.clicked.connect(self._add)

        layout = QFormLayout()
        layout.addRow(name_label, self.name_line)
        layout.addRow(saturday_label, self.saturday)
        layout.addWidget(add_button)
        self.setLayout(layout)

    def _add(self):
        response = self._manager.actions(Actions.add_position, [self.name_line.text(), self.saturday.currentText()])

        if response == ResponseStatus.success:
            QMessageBox.information(self, strs.ADD_VIEW_MSG, strs.POSITION_ADD_SUCC_MSG)
        elif response == ResponseStatus.fail:
            QMessageBox.warning(self, strs.ADD_VIEW_MSG, strs.POSITION_ADD_FAIL_MSG)

    def get_name(self):
        return self._name
