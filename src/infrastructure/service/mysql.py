from mysql.connector import connect


class MySQL:
    def __init__(self, config_storage):
        self.connection = connect(
            host=config_storage.HOST,
            user=config_storage.USER,
            password=config_storage.PASSWORD,
            database=config_storage.DATABASE
        )

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
