from sqlite3 import connect


class SQLite:
    def __init__(self, storege_path):
        self.connection = connect(storege_path)

    def execute_query(self, query: str):
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            return cursor

    def execute_query_complex(self, query: str, params: tuple):
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            return cursor

    def commit(self):
        self.connection.commit()

    def connection_close(self):
        self.connection.close()
