from configparser import ConfigParser
from collections import deque
import psycopg2

from project.utils.constants import DATABASE_CONFIG_PATH, DEFAULT_SECTION
from project.utils.enums import Actions, QueryType, Errors
from project.utils import strings as strs, sql_queries as sql


class DatabaseManager:

    def __init__(self):
        self._read_config()

    def actions(self, action, values=None):
        if action == Actions.login:
            return self._execute_query(sql.CHECK_CREDENTIALS, QueryType.select, values)
        elif action == Actions.all_employees:
            return self._execute_query(sql.SELECT_ALL_EMPLOYEES, QueryType.select)
        elif action == Actions.all_positions:
            return self._execute_query(sql.SELECT_ALL_POSITIONS, QueryType.select)
        elif action == Actions.all_uniforms:
            return self._execute_query(sql.SELECT_ALL_UNIFORMS, QueryType.select)
        elif action == Actions.all_uniform_pieces:
            return self._execute_query(sql.SELECT_ALL_UNIFORM_PIECES, QueryType.select)
        elif action == Actions.all_children:
            return self._execute_query(sql.SELECT_ALL_CHILDREN, QueryType.select)
        elif action == Actions.all_free_days:
            return self._execute_query(sql.SELECT_ALL_FREE_DAYS, QueryType.select)
        elif action == Actions.all_wages:
            return self._execute_query(sql.SELECT_ALL_WAGES, QueryType.select)
        elif action == Actions.add_employee:
            return self._execute_query(sql.INSERT_EMPLOYEE, QueryType.insert, values)
        elif action == Actions.add_position:
            return self._execute_query(sql.INSERT_POSITION, QueryType.insert, values)
        elif action == Actions.add_uniform:
            return self._execute_query(sql.INSERT_UNIFORM, QueryType.insert, values)
        elif action == Actions.add_uniform_piece:
            return self._execute_query(sql.INSERT_UNIFORM_PIECE, QueryType.insert, values)
        elif action == Actions.add_child:
            return self._execute_query(sql.INSERT_CHILD, QueryType.insert, values)
        elif action == Actions.add_free_days:
            return self._execute_query(sql.INSERT_FREE_DAYS, QueryType.insert, values)
        elif action == Actions.add_wage:
            return self._execute_query(sql.INSERT_WAGE, QueryType.insert, values)
        elif action == Actions.add_salary_1:
            return self._execute_query(sql.INSERT_SALARY_1, QueryType.insert, values)
        elif action == Actions.add_salary_2:
            return self._execute_query(sql.INSERT_SALARY_2, QueryType.insert, values)
        elif action == Actions.employee_salaries_1:
            return self._execute_query(sql.SELECT_EMPLOYEE_SALARIES_1, QueryType.select, values)
        elif action == Actions.employee_salaries_2:
            return self._execute_query(sql.SELECT_EMPLOYEE_SALARIES_2, QueryType.select, values)
        elif action == Actions.update_salary_1:
            return self._update_query(sql.UPDATE_SALARY_1, values)
        elif action == Actions.update_salary_2:
            return self._update_query(sql.UPDATE_SALARY_2, values)
        elif action == Actions.delete_salary_1:
            return self._execute_query(sql.DELETE_SALARY_1, QueryType.delete, values)
        elif action == Actions.delete_salary_2:
            return self._execute_query(sql.DELETE_SALARY_2, QueryType.delete, values)

    def _read_config(self, section=DEFAULT_SECTION):
        parser = ConfigParser()

        parser.read(DATABASE_CONFIG_PATH)

        if parser.has_section(section):
            params = parser.items(section)

            db = {param[0]: param[1] for param in params}
        else:
            # TODO Write error to a log
            raise Exception(strs.SECTION_NOT_FOUND_MSG.format(section=section))

        self.db = db

    def _execute_query(self, query, query_type, values=None):
        result = None
        conn = None

        try:
            params = self.db
            conn = psycopg2.connect(**params)

            cur = conn.cursor()

            cur.execute(query, values) if values else cur.execute(query)

            if query_type in [QueryType.update, QueryType.delete]:
                result = cur.statusmessage
            else:
                if cur.rowcount == 1:
                    result = cur.fetchone()
                elif cur.rowcount > 1:
                    result = cur.fetchall()

            conn.commit()

            cur.close()
        except Exception as error:
            # TODO Write error to a log
            print(strs.DATABASE_ERROR_MSG.format(error=error))

            result = Errors.database
        finally:
            if conn is not None:
                conn.close()

        return result

    def _update_query(self, query, values):
        values_deq = deque(values)
        values_deq.rotate(-1)

        return self._execute_query(query, QueryType.update, list(values_deq))
