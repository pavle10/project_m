from enum import Enum


class Actions(Enum):
    show = 0,
    login = 1,
    add_position = 2,
    add_employee = 3,
    add_uniform = 4,
    add_uniform_piece = 5,
    add_child = 6,
    add_free_days = 7,
    add_wage = 8,
    add_salary_1 = 9,
    add_salary_2 = 10,
    all_positions = 11,
    all_employees = 12,
    all_uniforms = 13,
    all_uniform_pieces = 14,
    all_children = 15,
    all_free_days = 16,
    all_wages = 17,
    all_salaries_1 = 18,
    all_salaries_2 = 19,
    employee_salaries_2 = 20,
    delete_salary_2 = 21


class Levels(Enum):
    everything = 0
    no_salary_2 = 1


class QueryType(Enum):
    select = 0,
    insert = 1,
    update = 2,
    delete = 3


class Responses(Enum):
    fail = 0,
    success = 1


class Errors(Enum):
    database = 0
