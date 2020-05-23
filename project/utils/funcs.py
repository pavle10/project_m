from project.utils.enums import Levels
import project.utils.strings as strs


def convert_level(value):
    if value == 0:
        return Levels.everything
    elif value == 1:
        return Levels.no_salary_2


def convert_saturday(value):
    return True if value == "Da" else False


def convert_date_to_string(date):
    return f"{date.year()}-{date.month()}-{date.day()}"


def data_manipulation_options():
    options = [strs.EMPLOYEE, strs.POSITION, strs.CHILD, strs.UNIFORM, strs.UNIFORM_PIECE,
               strs.FREE_DAY, strs.WAGE, strs.SALARY_1, strs.SALARY_2]

    return list(zip(range(len(options)), options))
