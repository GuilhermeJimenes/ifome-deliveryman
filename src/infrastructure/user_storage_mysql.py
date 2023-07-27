from src.domain.interfaces.user_interface import UserStorage
from src.domain.models.user_model import UserModel
from src.exceptions.custom_exceptions import NotFoundFail
from src.infrastructure.config.config_storage import ConfigStorage
from src.infrastructure.service.mysql import MySQL


class UserStorageMySQL(MySQL, UserStorage):
    def __init__(self):
        super(MySQL, self).__init__(ConfigStorage)
        self.create_table()

    def create_table(self):
        create_table_query = (
            "CREATE TABLE IF NOT EXISTS deliveryman ("
            "user_id VARCHAR(36) PRIMARY KEY,"
            "name VARCHAR(255) NOT NULL,"
            "email VARCHAR(255) NOT NULL"
            ")"
        )

        self.execute_query(create_table_query)
        self.commit()

    def get_all(self):
        get_all_query = "SELECT * FROM deliveryman"
        cursor = self.execute_query(get_all_query)

        if users := cursor.fetchall():
            return [UserModel(*user) for user in users]
        else:
            raise NotFoundFail('Deliveryman not found')

    def save(self, user):
        save_query = "INSERT INTO deliveryman (user_id, name, email) VALUES (%s, %s, %s)"
        save_params = (user.user_id, user.name, user.email)

        self.execute_query_complex(save_query, save_params)
        self.commit()
        self.connection_close()

    def get_by_id(self, user_id):
        get_by_id_query = "SELECT * FROM deliveryman WHERE user_id = %s"
        get_by_id_params = (user_id,)
        cursor = self.execute_query_complex(get_by_id_query, get_by_id_params)

        if user := cursor.fetchone():
            return UserModel(*user)
        else:
            raise NotFoundFail('Deliveryman not found')
