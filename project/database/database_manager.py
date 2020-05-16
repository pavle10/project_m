from configparser import ConfigParser
import psycopg2

from project.utils.constants import DATABASE_CONFIG_PATH
from project.utils.sql_queries import *
from project.enums.actions import Actions


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

            result = cur.fetchone()

            cur.close()
        except Exception as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

        return result

    def actions(self, action, values):
        if action == Actions.login:
            return self._check_credentials(values)

    def _check_credentials(self, values):
        query = CHECK_CREDENTIALS

        return self._execute_query(query, values)

