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
    employee_uniform_pieces = 20,
    employee_free_days = 21,
    employee_wage = 22,
    employee_salaries_1 = 23,
    employee_salaries_2 = 24,
    update_child = 25,
    update_uniform = 26,
    update_uniform_piece = 27,
    update_free_days = 28,
    update_wage = 29,
    update_salary_1 = 30,
    update_salary_2 = 31,
    delete_child = 32,
    delete_uniform = 33,
    delete_uniform_piece = 34,
    delete_free_days = 35,
    delete_wage = 36,
    delete_salary_1 = 37,
    delete_salary_2 = 38


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
