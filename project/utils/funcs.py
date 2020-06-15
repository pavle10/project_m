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


def printing_employee_name(name):
    if name is None:
        return name

    return " ".join(name.split(' ')[:2])


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


def append_style():
    text = "<style>"
    text += "@media print { body { margin: 1cm; } }"
    text += "h1 { text-align:center; margin-bottom: 15px; text-decoration: underline; }"

    text += "table, td, th { border-collapse: separate; border-color: red; border-style: solid; " \
            "border-width: 5px; text-align:center } "
    text += "th { background-color: powderblue; font-weight: bold; padding: 2px}"
    text += "td { padding: 2px }"

    text += "</style>"

    return text


def append_row(words, row_type, index=-1):
    text = "<tr>"

    if row_type == "Header":
        text += "<th></th>"

        for word in words:
            text += f"<th>{word}</th>"
    else:
        text += f"<td>{index}</td>"
        for data in words:
            text += f"<td>{data}</td>"

    text += "</tr>"

    return text


def append_table(data, table_header=None):
    text = "<table>"

    if table_header is not None:
        text += append_row(table_header, "Header")

    for index, entry in enumerate(data):
        text += append_row(entry, "Data", index+1)

    text += "</table>"

    return text


def append_salary_2_table(data):
    text = "<table>"

    text += f"<tr><td>Datum</td><td colspan=3>{data[0]}</td></tr>"
    text += f"<tr><td>Zaposleni</td><td colspan=3>{data[1]}</td></tr>"

    for entry in data[2:]:
        text += f"<tr><td>{entry[0]}</td><td>{entry[1]}</td><td>{entry[2]}</td><td>{entry[3]}</td></tr>"

    text += "</table>"

    return text


def append_salaries_1(data):
    table_header = ["Datum", "Neto", "Bruto"]
    title = strs.SALARY_1_LIST_TITLE.format(start_date=data["dates"][0][0], end_date=data["dates"][0][1])

    text = f"<h1>{title}</h1>"
    text += "<br>"

    for key, values in data.items():
        if key != "dates":
            data[key].append(calculate_average_salary(data[key]))
            text += f"<h2>{key}</h2><br>"
            text += append_table(data[key], table_header)
            text += "<br>"

    return text


def append_salary_2(data):
    title = strs.SALARY_2_LIST_TITLE.format(start_date=data["dates"][0][0], end_date=data["dates"][0][1])

    text = f"<h1>{title}</h1>"
    text += "<br>"

    for key, values in data.items():
        if key != "dates":
            text += append_salary_2_table(values)
            text += "<br>"

    return text


def create_html(title, data, table_header=None, report_type="Standard"):
    text = "<html>"
    text += append_style()
    text += "<body>"

    if report_type == "Standard":
        text += f"<h1>{title}</h1>"
        text += "<br>"
        text += append_table(data, table_header)
    elif report_type == strs.SALARY_1:
        text += append_salaries_1(data)
    elif report_type == strs.SALARY_2:
        text += append_salary_2(data)

    text += "</body>"
    text += "</html>"

    return text


def calculate_average_salary(data):
    avg_net = 0.0
    avg_gross = 0.0

    for entry in data:
        avg_net += int(entry[1])
        avg_gross += int(entry[2])

    return ["", str(avg_net / len(data)), str(avg_gross / len(data))]
