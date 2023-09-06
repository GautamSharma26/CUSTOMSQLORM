import mysql.connector


class MySqlConnection:
    def __init__(self, host, password, database, user):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def __enter__(self):
        self.conn = mysql.connector.connect(host=self.host, user=self.user, password=self.password,
                                            database=self.database)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()
