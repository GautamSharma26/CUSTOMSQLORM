class QueryBuilder:
    def __init__(self, table):
        self.table = table

    def read_all_data(self):
        return f"SELECT * FROM {self.table}"
