from SqlConnection.DbConnection import MySqlConnection
from SqlConnection.config import DB_CONFIG
from SqlConnection.SQlQuery import QueryBuilder


class Manager:
    def __init__(self, table):
        self.config = DB_CONFIG
        self.query_init = QueryBuilder(table=table)

    def _db_connection(self):
        return MySqlConnection(**self.config)

    def read_one(self):
        queue = self.query_init.read_all_data()
        with self._db_connection() as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(queue)
            data = cursor.fetchone()
        return data

    def fields_validation(self, *args):
        value = {args_data for args_data in args}
        return value

    def read_partial_field(self, *args):
        query = self.query_init.read_specific_data(args)
        with self._db_connection() as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query)
            output = cursor.fetchall()
        return output
