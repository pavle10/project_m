from PyQt5.QtWidgets import QMessageBox
import numpy as np

from project.utils.enums import Levels, ResponseStatus
import project.utils.strings as strs


def convert_level(value):
    if value == 0:
        return Levels.everything
    elif value == 1:
        return Levels.no_salary_2


def convert_saturday(value):
    return True if value == strs.YES else False


def convert_date_to_string(date):
    return f"{date.year()}-{date.month()}-{date.day()}"


def convert_to_int(values, indices):
    try:
        for index in indices:
            values[index] = 0 if values[index] == "" else int(values[index])
    except ValueError:
        # TODO Write to log
        return False

    return True


def employee_unique_name(employee):
    return f"{employee.get_first_name()} {employee.get_last_name()} {employee.get_identity_number()}"


def transform_salary_data(employee_name, values):
    data = list(values)
    data.append(employee_name)

    return data


def show_message(parent, status, title, message):
    if status == ResponseStatus.success:
        QMessageBox.information(parent, title, message)
    else:
        QMessageBox.warning(parent, title, message)


def from_days(num_days):
    years = 0
    months = 0

    delta = 365
    count = 1
    while num_days - delta >= 0:
        num_days -= delta
        years += 1
        count = (count + 1) % 4
        if count:
            delta = 365
        else:
            delta = 366

    delta = 31
    count = 1
    while num_days - delta >= 0:
        num_days -= delta
        months += 1
        count += 1
        if count == 2:
            if years != 0 and years % 3 == 0:
                delta = 29
            else:
                delta = 28
        elif count in [3, 5, 7, 8, 10, 12]:
            delta = 31
        else:
            delta = 30

    return [years, months, num_days]


def to_days(years, months, days):
    leap_years = years // 4
    days += 366 * leap_years + 365 * (years - leap_years)

    months_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if years != 0 and years % 3 == 0:
        months_list[1] = 29

    for i in range(months):
        days += months_list[i]

    return days


def print_days(before_m):
    before_m = from_days(before_m)

    return f"{before_m[0]}g {before_m[1]}m {before_m[2]}d"


def check_required_fields(*args):
    for arg in args:
        if arg == "":
            return False

    return True


def is_query_successful(response):
    if response.get_status() == ResponseStatus.success:
        if len(response.get_data()) > 0:
            return True

    return False


def count_free_days(start_date, end_date):
    return int(np.busday_count(start_date, end_date))
