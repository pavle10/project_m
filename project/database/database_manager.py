from configparser import ConfigParser
import psycopg2

from project.utils.constants import DATABASE_CONFIG_PATH
from project.models.position import Position
from project.models.employee import Employee
from project.models.uniform import Uniform
from project.enums.actions import Actions
from project.enums.query_type import QueryType
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

    def _execute_query(self, query, query_type, values=None):
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

            if query_type == QueryType.select:
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
        elif action == Actions.add_employee:
            return self._insert_employee(values)
        elif action == Actions.add_position:
            return self._insert_position(values)
        elif action == Actions.add_uniform:
            return self._insert_uniform(values)

    def _check_credentials(self, values):
        query = CHECK_CREDENTIALS

        return self._execute_query(query, QueryType.select, values)

    def _get_employees(self):
        query = SELECT_ALL_EMPLOYEES
        employees = list()

        result = self._execute_query(query, QueryType.select)

        for res in result:
            employee = Employee(res[0], res[1], res[2], res[3], res[4],
                                res[5], res[6], res[7], res[8], res[9],
                                res[10], res[11], res[12], res[13], res[14], res[15])
            employees.append(employee)

        return employees

    def _get_positions(self):
        query = SELECT_ALL_POSITIONS

        result = self._execute_query(query, QueryType.select)

        return [Position(pos[0], pos[1], pos[2]) for pos in result]

    def _get_uniforms(self):
        query = SELECT_ALL_UNIFOMRS

        result = self._execute_query(query, QueryType.select)

        return [Uniform(uni[0], uni[1]) for uni in result]

    def _insert_employee(self, values):
        insert_query = INSERT_EMPLOYEE

        result = self._execute_query(insert_query, QueryType.insert, values)

        if result:
            return self._execute_query(SELECT_EMPLOYEE_BY_IDENTITY_NUMBER, QueryType.select, [values[3]])

        return None

    def _insert_position(self, values):
        insert_query = INSERT_POSITION
        values[1] = convert_saturday(values[1])

        result = self._execute_query(insert_query, QueryType.insert, values)

        if result:
            return self._execute_query(SELECT_POSITION_BY_NAME, QueryType.select, [values[0]])

        return None

    def _insert_uniform(self, values):
        insert_query = INSERT_UNIFORM

        result = self._execute_query(insert_query, QueryType.insert, values)

        if result:
            return self._execute_query(SELECT_UNIFORM_BY_NAME, QueryType.select, [values[0]])

