from configparser import ConfigParser
import psycopg2

from project.utils.constants import DATABASE_CONFIG_PATH
from project.models.position import Position
from project.models.employee import Employee
from project.models.uniform import Uniform
from project.models.uniform_piece import UniformPiece
from project.models.child import Child
from project.models.free_days import FreeDays
from project.models.wage import Wage
from project.enums.actions import Actions
from project.utils.sql_queries import *
from project.utils.funcs import *


class DatabaseManager:

    def __init__(self, manager):
        self.action_manager = manager
        self.db = self._read_config()

    def _read_config(self, section="postgresql"):
        parser = ConfigParser()

        parser.read(DATABASE_CONFIG_PATH)

        db = {}

        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception(f"Section {section} not found!")

        return db

    def _execute_query(self, query, values=None):
        result = None
        conn = None

        try:
            params = self.db
            conn = psycopg2.connect(**params)

            cur = conn.cursor()

            if values:
                cur.execute(query, values)
            else:
                cur.execute(query)

            if cur.rowcount == 1:
                result = cur.fetchone()
            elif cur.rowcount > 1:
                result = cur.fetchall()
            else:
                result = cur.statusmessage

            conn.commit()

            cur.close()
        except Exception as error:
            print(f"DB error: {error}")
        finally:
            if conn is not None:
                conn.close()

        return result

    def actions(self, action, values=None):
        if action == Actions.login:
            return self._check_credentials(values)
        elif action == Actions.all_employees:
            return self._get_employees()
        elif action == Actions.all_positions:
            return self._get_positions()
        elif action == Actions.all_uniforms:
            return self._get_uniforms()
        elif action == Actions.all_uniform_pieces:
            return self._get_uniform_pieces()
        elif action == Actions.all_children:
            return self._get_children()
        elif action == Actions.all_free_days:
            return self._get_all_free_days()
        elif action == Actions.all_wages:
            return self._get_all_wages()
        elif action == Actions.add_employee:
            return self._insert_employee(values)
        elif action == Actions.add_position:
            return self._insert_position(values)
        elif action == Actions.add_uniform:
            return self._insert_uniform(values)
        elif action == Actions.add_uniform_piece:
            return self._insert_uniform_piece(values)
        elif action == Actions.add_child:
            return self._insert_child(values)
        elif action == Actions.add_free_days:
            return self._insert_free_days(values)
        elif action == Actions.add_wage:
            return self._insert_wage(values)
        elif action == Actions.add_salary_1:
            return self._insert_salary_1(values)
        elif action == Actions.add_salary_2:
            return self._insert_salary_2(values)

    def _check_credentials(self, values):
        query = CHECK_CREDENTIALS

        return self._execute_query(query, values)

    def _get_employees(self):
        query = SELECT_ALL_EMPLOYEES
        employees = list()

        result = self._execute_query(query)

        for res in result:
            employee = Employee(res[0], res[1], res[2], res[3], res[4],
                                res[5], res[6], res[7], res[8], res[9],
                                res[10], res[11], res[12], res[13], res[14], res[15])
            employees.append(employee)

        return employees

    def _get_positions(self):
        query = SELECT_ALL_POSITIONS

        result = self._execute_query(query)

        return [Position(pos[0], pos[1], pos[2]) for pos in result]

    def _get_uniforms(self):
        query = SELECT_ALL_UNIFORMS

        result = self._execute_query(query)

        return [Uniform(uni[0], uni[1]) for uni in result]

    def _get_uniform_pieces(self):
        query = SELECT_ALL_UNIFORM_PIECES
        uniform_pieces = list()

        result = self._execute_query(query)

        for res in result:
            uniform_piece = UniformPiece(res[0], res[1], res[2], res[3], res[4], res[5], res[6])
            uniform_pieces.append(uniform_piece)

        return uniform_pieces

    def _get_children(self):
        query = SELECT_ALL_CHILDREN

        result = self._execute_query(query)

        return [Child(res[0], res[1], res[2], res[3], res[4]) for res in result]

    def _get_all_free_days(self):
        query = SELECT_ALL_FREE_DAYS

        result = self._execute_query(query)

        return [FreeDays(res[0], res[1], res[2], res[3], res[4], res[5]) for res in result]

    def _get_all_wages(self):
        query = SELECT_ALL_WAGES

        result = self._execute_query(query)

        return [Wage(res[0], res[1], res[2], res[3], res[4]) for res in result]

    def _insert_employee(self, values):
        insert_query = INSERT_EMPLOYEE

        return self._execute_query(insert_query, values)

    def _insert_position(self, values):
        insert_query = INSERT_POSITION
        values[1] = convert_saturday(values[1])

        return self._execute_query(insert_query, values)

    def _insert_uniform(self, values):
        insert_query = INSERT_UNIFORM

        return self._execute_query(insert_query, values)

    def _insert_uniform_piece(self, values):
        insert_query = INSERT_UNIFORM_PIECE

        return self._execute_query(insert_query, values)

    def _insert_child(self, values):
        insert_query = INSERT_CHILD

        return self._execute_query(insert_query, values)

    def _insert_free_days(self, values):
        insert_query = INSERT_FREE_DAYS

        return self._execute_query(insert_query, values)

    def _insert_wage(self, values):
        insert_query = INSERT_WAGE

        return self._execute_query(insert_query, values)

    def _insert_salary_1(self, values):
        insert_query = INSERT_SALARY_1

        return self._execute_query(insert_query, values)

    def _insert_salary_2(self, values):
        insert_query = INSERT_SALARY_2

        return self._execute_query(insert_query, values)

