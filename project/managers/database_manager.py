from configparser import ConfigParser
from collections import deque
import psycopg2

from project.utils.constants import DATABASE_CONFIG_PATH, DEFAULT_SECTION
from project.utils.enums import Actions, QueryType, ResponseStatus
from project.utils import strings as strs, sql_queries as sql, funcs
from project.models.response import Response
from project.models.position import Position
from project.models.employee import Employee
from project.models.uniform import Uniform
from project.models.uniform_piece import UniformPiece
from project.models.child import Child
from project.models.free_days import FreeDays
from project.models.wage import Wage


class DatabaseManager:

    def __init__(self):
        self._read_config()

    def actions(self, action, values=None):
        if action == Actions.login:
            return self._login(values)
        elif action == Actions.all_employees:
            return self._get_employees()
        elif action == Actions.all_positions:
            return self._get_positions()
        elif action == Actions.all_uniforms:
            return self._get_uniforms()
        elif action == Actions.all_uniform_pieces:
            return self._get_uniform_pieces()
        elif action == Actions.all_children:
            return self._get_all_children()
        elif action == Actions.all_free_days:
            return self._get_all_free_days()
        elif action == Actions.all_wages:
            return self._get_wages()
        elif action == Actions.add_employee:
            return self._add_employee(values)
        elif action == Actions.add_position:
            return self._add_position(values)
        elif action == Actions.add_uniform:
            return self._add_uniform(values)
        elif action == Actions.add_uniform_piece:
            return self._add_uniform_piece(values)
        elif action == Actions.add_child:
            return self._add_child(values)
        elif action == Actions.add_free_days:
            return self._add_free_days(values)
        elif action == Actions.add_wage:
            return self._add_wage(values)
        elif action == Actions.add_salary_1:
            return self._add_salary_1(values)
        elif action == Actions.add_salary_2:
            return self._add_salary_2(values)
        elif action == Actions.employee_salaries_1:
            return self._execute_query(sql.SELECT_EMPLOYEE_SALARIES_1, QueryType.select, values)
        elif action == Actions.employee_salaries_2:
            return self._execute_query(sql.SELECT_EMPLOYEE_SALARIES_2, QueryType.select, values)
        elif action == Actions.update_employee:
            return self._update_query(sql.UPDATE_EMPLOYEE, values)
        elif action == Actions.update_position:
            return self._update_query(sql.UPDATE_POSITION, values)
        elif action == Actions.update_child:
            return self._update_query(sql.UPDATE_CHILD, values)
        elif action == Actions.update_uniform:
            return self._update_query(sql.UPDATE_UNIFORM, values)
        elif action == Actions.update_uniform_piece:
            return self._update_query(sql.UPDATE_UNIFORM_PIECE, values)
        elif action == Actions.update_free_days:
            return self._update_query(sql.UPDATE_FREE_DAYS, values)
        elif action == Actions.update_wage:
            return self._update_wage(values)
        elif action == Actions.update_salary_1:
            return self._update_salary_1(values)
        elif action == Actions.update_salary_2:
            return self._update_salary_2(values)
        elif action == Actions.delete_employee:
            return self._execute_query(sql.DELETE_EMPLOYEE, QueryType.delete, values)
        elif action == Actions.delete_position:
            return self._execute_query(sql.DELETE_POSITION, QueryType.delete, values)
        elif action == Actions.delete_child:
            return self._execute_query(sql.DELETE_CHILD, QueryType.delete, values)
        elif action == Actions.delete_uniform:
            return self._execute_query(sql.DELETE_UNIFORM, QueryType.delete, values)
        elif action == Actions.delete_uniform_piece:
            return self._execute_query(sql.DELETE_UNIFORM_PIECE, QueryType.delete, values)
        elif action == Actions.delete_free_days:
            return self._execute_query(sql.DELETE_FREE_DAYS, QueryType.delete, values)
        elif action == Actions.delete_wage:
            return self._delete_wage(values)
        elif action == Actions.delete_salary_1:
            return self._delete_salary_1(values)
        elif action == Actions.delete_salary_2:
            return self._delete_salary_2(values)

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
        status = ResponseStatus.success
        data = None
        conn = None

        try:
            params = self.db
            conn = psycopg2.connect(**params)

            cur = conn.cursor()

            cur.execute(query, values) if values else cur.execute(query)

            if query_type in [QueryType.select, QueryType.insert]:
                if cur.rowcount == 0:
                    # Do not set status to fail, because some queries are successful even if the rowcount == 0
                    data = list()
                elif cur.rowcount == 1:
                    data = [cur.fetchone()]
                elif cur.rowcount > 1:
                    data = cur.fetchall()

            message = cur.statusmessage

            print(f"Query: {query}")
            print(f"DB Data: {data}")
            print(f"DB Message: {message}\n")

            conn.commit()

            cur.close()
        except Exception as error:
            # TODO Write error to a log
            status = ResponseStatus.fail
            message = strs.DATABASE_ERROR_MSG.format(error=error)

            print(message)

        finally:
            if conn is not None:
                conn.close()

        return Response(status, message, data)

    def _update_query(self, query, values):
        values_deq = deque(values)
        values_deq.rotate(-1)

        return self._execute_query(query, QueryType.update, list(values_deq))

    def _login(self, values):
        response = self._execute_query(sql.CHECK_CREDENTIALS, QueryType.select, values)

        if response.get_status() == ResponseStatus.success and len(response.get_data()) == 0:
            response.set_status(ResponseStatus.fail)
            response.set_message(strs.WRONG_CREDENTIALS_MSG)

        return response

    def _get_employees(self):
        response = self._execute_query(sql.SELECT_ALL_EMPLOYEES, QueryType.select)

        if response.get_status() == ResponseStatus.success:
            data = [Employee.from_values(values) for values in response.get_data()]
            response.set_data(data)

        return response

    def _get_positions(self):
        response = self._execute_query(sql.SELECT_ALL_POSITIONS, QueryType.select)

        if response.get_status() == ResponseStatus.success:
            data = [Position.from_values(values) for values in response.get_data()]
            response.set_data(data)

        return response

    def _get_uniforms(self):
        response = self._execute_query(sql.SELECT_ALL_UNIFORMS, QueryType.select)

        if response.get_status() == ResponseStatus.success:
            data = [Uniform.from_values(values) for values in response.get_data()]
            response.set_data(data)

        return response

    def _get_uniform_pieces(self):
        response = self._execute_query(sql.SELECT_ALL_UNIFORM_PIECES, QueryType.select)

        if response.get_status() == ResponseStatus.success:
            data = [UniformPiece.from_values(values) for values in response.get_data()]
            response.set_data(data)

        return response

    def _get_all_children(self):
        response = self._execute_query(sql.SELECT_ALL_CHILDREN, QueryType.select)

        if response.get_status() == ResponseStatus.success:
            data = [Child.from_values(values) for values in response.get_data()]
            response.set_data(data)

        return response

    def _get_all_free_days(self):
        response = self._execute_query(sql.SELECT_ALL_FREE_DAYS, QueryType.select)

        if response.get_status() == ResponseStatus.success:
            data = [FreeDays.from_values(values) for values in response.get_data()]
            response.set_data(data)

        return response

    def _get_wages(self):
        response = self._execute_query(sql.SELECT_ALL_WAGES, QueryType.select)

        if response.get_status() == ResponseStatus.success:
            data = [Wage.from_values(values) for values in response.get_data()]
            response.set_data(data)

        return response

    def _add_employee(self, values):
        response = self._execute_query(sql.INSERT_EMPLOYEE, QueryType.insert, values)

        if funcs.is_query_successful(response):
            response.set_data(Employee.from_values(response.get_data()[0]))
            response.set_message(strs.EMPLOYEE_ADD_SUCC_MSG)
        else:
            response.set_status(ResponseStatus.fail)
            response.set_message(strs.EMPLOYEE_ADD_FAIL_MSG)

        return response

    def _add_position(self, values):
        response = self._execute_query(sql.INSERT_POSITION, QueryType.insert, values)

        if funcs.is_query_successful(response):
            response.set_data(Position.from_values(response.get_data()[0]))
            response.set_message(strs.POSITION_ADD_SUCC_MSG)
        else:
            response.set_status(ResponseStatus.fail)
            response.set_message(strs.POSITION_ADD_FAIL_MSG)

        return response

    def _add_child(self, values):
        response = self._execute_query(sql.INSERT_CHILD, QueryType.insert, values)

        if funcs.is_query_successful(response):
            response.set_data(Child.from_values(response.get_data()[0]))
            response.set_message(strs.CHILD_ADD_SUCC_MSG)
        else:
            response.set_status(ResponseStatus.fail)
            response.set_message(strs.CHILD_ADD_FAIL_MSG)

        return response

    def _add_uniform(self, values):
        response = self._execute_query(sql.INSERT_UNIFORM, QueryType.insert, values)

        if funcs.is_query_successful(response):
            response.set_data(Uniform.from_values(response.get_data()[0]))
            response.set_message(strs.UNIFORM_ADD_SUCC_MSG)
        else:
            response.set_status(ResponseStatus.fail)
            response.set_message(strs.UNIFORM_ADD_FAIL_MSG)

        return response

    def _add_uniform_piece(self, values):
        response = self._execute_query(sql.INSERT_UNIFORM_PIECE, QueryType.insert, values)

        if funcs.is_query_successful(response):
            response.set_data(UniformPiece.from_values(response.get_data()[0]))
            response.set_message(strs.UNIFORM_PIECE_ADD_SUCC_MSG)
        else:
            response.set_status(ResponseStatus.fail)
            response.set_message(strs.UNIFORM_PIECE_ADD_FAIL_MSG)

        return response

    def _add_free_days(self, values):
        response = self._execute_query(sql.INSERT_FREE_DAYS, QueryType.insert, values)

        if funcs.is_query_successful(response):
            response.set_data(FreeDays.from_values(response.get_data()[0]))
            response.set_message(strs.FREE_DAYS_ADD_SUCC_MSG)
        else:
            response.set_status(ResponseStatus.fail)
            response.set_message(strs.FREE_DAYS_ADD_FAIL_MSG)

        return response

    def _add_wage(self, values):
        response = self._execute_query(sql.INSERT_WAGE, QueryType.insert, values)

        if funcs.is_query_successful(response):
            response.set_data(Wage.from_values(response.get_data()[0]))
            response.set_message(strs.WAGE_ADD_SUCC_MSG)
        else:
            response.set_status(ResponseStatus.fail)
            response.set_message(strs.WAGE_ADD_FAIL_MSG)

        return response

    def _add_salary_1(self, values):
        response = self._execute_query(sql.INSERT_SALARY_1, QueryType.insert, values)

        if funcs.is_query_successful(response):
            response.set_message(strs.SALARY_1_ADD_SUCC_MSG)
        else:
            response.set_status(ResponseStatus.fail)
            response.set_message(strs.SALARY_1_ADD_FAIL_MSG)

        return response

    def _add_salary_2(self, values):
        response = self._execute_query(sql.INSERT_SALARY_2, QueryType.insert, values)

        if funcs.is_query_successful(response):
            response.set_message(strs.SALARY_2_ADD_SUCC_MSG)
        else:
            response.set_status(ResponseStatus.fail)
            response.set_message(strs.SALARY_2_ADD_FAIL_MSG)

        return response

    def _update_wage(self, values):
        response = self._update_query(sql.UPDATE_WAGE, values)

        if response.get_status() == ResponseStatus.success:
            response.set_message(strs.WAGE_UPD_SUCC_MSG)
        else:
            response.set_status(ResponseStatus.fail)
            response.set_message(strs.WAGE_UPD_FAIL_MSG)

        return response

    def _update_salary_1(self, values):
        response = self._update_query(sql.UPDATE_SALARY_1, values)

        if response.get_status() == ResponseStatus.success:
            response.set_message(strs.SALARY_1_UPD_SUCC_MSG)
        else:
            response.set_status(ResponseStatus.fail)
            response.set_message(strs.SALARY_1_UPD_FAIL_MSG)

        return response

    def _update_salary_2(self, values):
        response = self._update_query(sql.UPDATE_SALARY_2, values)

        if response.get_status() == ResponseStatus.success:
            response.set_message(strs.SALARY_2_UPD_SUCC_MSG)
        else:
            response.set_status(ResponseStatus.fail)
            response.set_message(strs.SALARY_2_UPD_FAIL_MSG)

        return response

    def _delete_wage(self, values):
        response = self._execute_query(sql.DELETE_WAGE, QueryType.delete, values)

        if response.get_status() == ResponseStatus.success:
            response.set_message(strs.WAGE_DEL_SUCC_MSG)
        else:
            response.set_status(ResponseStatus.fail)
            response.set_message(strs.WAGE_DEL_FAIL_MSG)

        return response

    def _delete_salary_1(self, values):
        response = self._execute_query(sql.DELETE_SALARY_1, QueryType.delete, values)

        if response.get_status() == ResponseStatus.success:
            response.set_message(strs.SALARY_1_DEL_SUCC_MSG)
        else:
            response.set_status(ResponseStatus.fail)
            response.set_message(strs.SALARY_1_DEL_FAIL_MSG)

        return response

    def _delete_salary_2(self, values):
        response = self._execute_query(sql.DELETE_SALARY_2, QueryType.delete, values)

        if response.get_status() == ResponseStatus.success:
            response.set_message(strs.SALARY_2_DEL_SUCC_MSG)
        else:
            response.set_status(ResponseStatus.fail)
            response.set_message(strs.SALARY_2_DEL_FAIL_MSG)

        return response

