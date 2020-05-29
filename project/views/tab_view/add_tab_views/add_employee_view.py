from project.views.tab_view.add_tab_views.add_view import AddView
from project.utils.enums import Actions, ResponseStatus
from project.utils import strings as strs, funcs
from project.models.my_widgets import *


class AddEmployeeView(AddView):

    def __init__(self, name, manager, *args, **kwargs):
        super(AddEmployeeView, self).__init__(*args, **kwargs)
        self._name = name
        self._manager = manager

        self._init_ui()

    def _init_ui(self):
        first_name_label = MyLabel(strs.PRESENT_EMPLOYEE_HDR[0], is_required=True)
        self.first_name_line = MyEditLine()
        first_name_label.setBuddy(self.first_name_line)

        last_name_label = MyLabel(strs.PRESENT_EMPLOYEE_HDR[1], is_required=True)
        self.last_name_line = MyEditLine()
        last_name_label.setBuddy(self.last_name_line)

        fathers_name_label = MyLabel(strs.PRESENT_EMPLOYEE_HDR[2])
        self.fathers_name_line = MyEditLine()
        fathers_name_label.setBuddy(self.fathers_name_line)

        identity_number_label = MyLabel(strs.PRESENT_EMPLOYEE_HDR[3], is_required=True)
        self.identity_number_line = MyEditLine()
        identity_number_label.setBuddy(self.identity_number_line)

        personal_card_label = MyLabel(strs.PRESENT_EMPLOYEE_HDR[4])
        self.personal_card_line = MyEditLine()
        personal_card_label.setBuddy(self.personal_card_line)

        qualification_label = MyLabel(strs.PRESENT_EMPLOYEE_HDR[5])
        self.qualification_line = MyEditLine()
        qualification_label.setBuddy(self.qualification_line)

        position_label = MyLabel(strs.PRESENT_EMPLOYEE_HDR[6], is_required=True)
        self.position_box = MyComboBox()
        for index, position in enumerate(self._get_positions()):
            self.position_box.insertItem(index, position.get_name())
        position_label.setBuddy(self.position_box)

        saint_day_label = MyLabel(strs.PRESENT_EMPLOYEE_HDR[7])
        self.saint_day_line = MyEditLine()
        saint_day_label.setBuddy(self.saint_day_line)

        address_label = MyLabel(strs.PRESENT_EMPLOYEE_HDR[8], is_required=True)
        self.address_line = MyEditLine()
        address_label.setBuddy(self.address_line)

        account_label = MyLabel(strs.PRESENT_EMPLOYEE_HDR[9])
        self.account_line = MyEditLine()
        account_label.setBuddy(self.account_line)

        before_m_label = MyLabel(strs.PRESENT_EMPLOYEE_HDR[10])
        years_label = MyLabelShort(strs.YEARS)
        self.years_line = MyEditLineShort()
        months_label = MyLabelShort(strs.MONTHS)
        self.months_line = MyEditLineShort()
        days_label = MyLabelShort(strs.DAYS)
        self.days_line = MyEditLineShort()
        before_layout = QHBoxLayout()
        before_layout.addWidget(years_label)
        before_layout.addWidget(self.years_line)
        before_layout.addWidget(months_label)
        before_layout.addWidget(self.months_line)
        before_layout.addWidget(days_label)
        before_layout.addWidget(self.days_line)

        start_date_label = MyLabel(strs.PRESENT_EMPLOYEE_HDR[11], is_required=True)
        self.start_date_line = MyEditDate()
        start_date_label.setBuddy(self.start_date_line)

        home_number_label = MyLabel(strs.PRESENT_EMPLOYEE_HDR[12])
        self.home_number_line = MyEditLine()
        home_number_label.setBuddy(self.home_number_line)

        mobile_number_label = MyLabel(strs.PRESENT_EMPLOYEE_HDR[13])
        self.mobile_number_line = MyEditLine()
        mobile_number_label.setBuddy(self.mobile_number_line)

        situation_label = MyLabel(strs.PRESENT_EMPLOYEE_HDR[14])
        self.situation_line = MyEditLine()
        situation_label.setBuddy(self.situation_line)

        add_button = MyButton(strs.ADD_BTN)
        add_button.clicked.connect(self._add)

        layout = QFormLayout()
        layout.addRow(first_name_label, self.first_name_line)
        layout.addRow(last_name_label, self.last_name_line)
        layout.addRow(fathers_name_label, self.fathers_name_line)
        layout.addRow(identity_number_label, self.identity_number_line)
        layout.addRow(personal_card_label, self.personal_card_line)
        layout.addRow(qualification_label, self.qualification_line)
        layout.addRow(position_label, self.position_box)
        layout.addRow(saint_day_label, self.saint_day_line)
        layout.addRow(address_label, self.address_line)
        layout.addRow(account_label, self.account_line)
        layout.addRow(before_m_label, before_layout)
        layout.addRow(start_date_label, self.start_date_line)
        layout.addRow(home_number_label, self.home_number_line)
        layout.addRow(mobile_number_label, self.mobile_number_line)
        layout.addRow(situation_label, self.situation_line)
        layout.addWidget(add_button)
        self.setLayout(layout)

    def _add(self):
        before_m = [self.years_line.text(), self.months_line.text(), self.days_line.text()]
        values = [self.first_name_line.text(), self.last_name_line.text(), self.fathers_name_line.text(),
                  self.identity_number_line.text(), self.personal_card_line.text(), self.qualification_line.text(),
                  self.position_box.currentText(), self.saint_day_line.text(), self.address_line.text(),
                  self.account_line.text(), before_m, self.start_date_line.date().toPyDate(),
                  self.home_number_line.text(), self.mobile_number_line.text(), self.situation_line.text()]

        response = self._manager.actions(Actions.add_employee, values)

        funcs.show_message(self, response.get_status(), strs.ADD_VIEW_MSG, response.get_message())

        if response.get_status() == ResponseStatus.success:
            self._clear()

    def _get_positions(self):
        return self._manager.actions(Actions.all_positions)

    def _clear(self):
        self.first_name_line.clear()
        self.last_name_line.clear()
        self.fathers_name_line.clear()
        self.identity_number_line.clear()
        self.personal_card_line.clear()
        self.qualification_line.clear()
        self.position_box.setCurrentIndex(0)
        self.saint_day_line.clear()
        self.address_line.clear()
        self.account_line.clear()
        self.years_line.clear()
        self.months_line.clear()
        self.days_line.clear()
        self.start_date_line.setDate(cons.DEFAULT_END_DATE)
        self.home_number_line.clear()
        self.mobile_number_line.clear()
        self.situation_line.clear()

    def get_name(self):
        return self._name
