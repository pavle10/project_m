from configparser import ConfigParser
import psycopg2

from project.utils.constants import DATABASE_CONFIG_PATH
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
        elif action == Actions.init_employees:
            return self._get_employees()
        elif action == Actions.init_positions:
            return self._get_positions()
        elif action == Actions.add_position:
            return self._insert_position(values)

    def _check_credentials(self, values):
        query = CHECK_CREDENTIALS

        return self._execute_query(query, QueryType.select, values)

    def _get_employees(self):
        query = SELECT_ALL_EMPLOYEES

        return self._execute_query(query, QueryType.select)

    def _get_positions(self):
        query = SELECT_ALL_POSITIONS

        return self._execute_query(query, QueryType.select)

    def _insert_position(self, values):
        insert_query = INSERT_POSITION
        values[1] = convert_saturday(values[1])

        result = self._execute_query(insert_query, QueryType.insert, values)

        if result:
            return self._execute_query(SELECT_pOSITION_BY_NAME, QueryType.select, [values[0]])

