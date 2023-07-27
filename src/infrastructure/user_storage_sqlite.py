from src.domain.constants import STORAGE_SQLITE_PATH
from src.domain.interfaces.user_interface import UserStorage
from src.domain.models.user_model import UserModel
from src.exceptions.custom_exceptions import NotFoundFail
from src.infrastructure.service.sqlite import SQLite


class UserStorageSQLite(SQLite, UserStorage):
    def __init__(self):
        super(SQLite, self).__init__(STORAGE_SQLITE_PATH)
        self.create_table()

    def create_table(self):
        create_table_query = (
            "CREATE TABLE IF NOT EXISTS deliveryman ("
            "user_id TEXT PRIMARY KEY,"
            "name TEXT NOT NULL,"
            "email TEXT NOT NULL"
            ")"
        )

        self.execute_query(create_table_query)

    def get_all(self):
        get_all_query = "SELECT * FROM deliveryman"
        cursor = self.execute_query(get_all_query)

        if users := cursor.fetchall():
            return [UserModel(*user) for user in users]
        else:
            raise NotFoundFail('Deliveryman not found')

    def save(self, user):
        save_query = "INSERT INTO deliveryman (user_id, name, email) VALUES (?, ?, ?)"
        save_params = (user.user_id, user.name, user.email)

        self.execute_query_complex(save_query, save_params)
        self.commit()

    def get_by_id(self, user_id):
        get_by_id_query = "SELECT * FROM deliveryman WHERE user_id = ?"
        get_by_id_params = (user_id,)

        cursor = self.execute_query_complex(get_by_id_query, get_by_id_params)

        if user := cursor.fetchone():
            return UserModel(*user)
        else:
            raise NotFoundFail('Deliveryman not found')
