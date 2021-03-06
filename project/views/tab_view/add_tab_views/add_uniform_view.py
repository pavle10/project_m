from project.views.tab_view.add_tab_views.add_view import AddView
from project.utils.enums import Actions, ResponseStatus
from project.utils import strings as strs, funcs
from project.models.my_widgets import *


class AddUniformView(AddView):

    def __init__(self, name, manager, *args, **kwargs):
        super(AddUniformView, self).__init__(*args, **kwargs)
        self._name = name
        self._manager = manager

        self._init_ui()

    def _init_ui(self):
        name_label = MyLabel(strs.PRESENT_UNIFORM_HDR[0], is_required=True)
        self.name_line = MyEditLine()
        name_label.setBuddy(self.name_line)

        add_button = MyButton(strs.ADD_BTN)
        add_button.clicked.connect(self._add)

        layout = QFormLayout()
        layout.addRow(name_label, self.name_line)
        layout.addWidget(add_button)
        self.setLayout(layout)

    def _add(self):
        response = self._manager.actions(Actions.add_uniform, [self.name_line.text()])

        funcs.show_message(self, response.get_status(), strs.ADD_VIEW_MSG, response.get_message())

        if response.get_status() == ResponseStatus.success:
            self._clear()

    def _clear(self):
        self.name_line.clear()

    def get_name(self):
        return self._name

    def update(self):
        pass
