from SqlConnection.DbConnection import MySqlConnection
from SqlConnection.config import DB_CONFIG
from SqlConnection.SQlQuery import QueryBuilder


class Manager:
    def __init__(self,table):
        self.config = DB_CONFIG
        self.query_init = QueryBuilder(table=table)

    def _db_connection(self):
        return MySqlConnection(**self.config)

    def read_all(self):
        queue = self.query_init.read_all_data()
        with self._db_connection() as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(queue)
            data = cursor.fetchall()
        return data
