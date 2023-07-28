from src.domain.constants import STORAGE_SQLITE_PATH, TABLE_SQLITE_DELIVERYMANS
from src.domain.interfaces.deliveryman_interface import DeliverymanStorage
from src.domain.models.deliveryman_model import DeliverymanModel
from src.exceptions.custom_exceptions import NotFoundFail
from src.infrastructure.service.sqlite import SQLite


class DeliverymanStorageSQLite(SQLite, DeliverymanStorage):
    def __init__(self):
        table_path = f"{STORAGE_SQLITE_PATH}{TABLE_SQLITE_DELIVERYMANS}"
        super(DeliverymanStorageSQLite, self).__init__(table_path)
        self.create_table()

    def create_table(self):
        create_table_query = (
            "CREATE TABLE IF NOT EXISTS deliveryman ("
            "deliveryman_id TEXT PRIMARY KEY,"
            "name TEXT NOT NULL,"
            "email TEXT NOT NULL"
            ")"
        )

        self.execute_query_one(create_table_query)

    def get_all(self):
        get_all_query = "SELECT * FROM deliveryman"
        cursor = self.execute_query_many(get_all_query)

        if deliverymans := cursor.fetchall():
            return [DeliverymanModel(*deliveryman) for deliveryman in deliverymans]
        else:
            raise NotFoundFail('Deliveryman not found')

    def get_by_id(self, value_id, key_id="deliveryman_id", return_fields="*"):
        get_by_id_query = f"SELECT {return_fields} FROM deliveryman WHERE {key_id} = ?"
        get_by_id_params = (value_id,)
        data_deliveryman = self.execute_query_one(get_by_id_query, get_by_id_params)

        if data_deliveryman and return_fields == "*":
            return DeliverymanModel(*data_deliveryman)
        elif data_deliveryman and return_fields != "*":
            return data_deliveryman
        else:
            raise NotFoundFail('Deliveryman not found')

    def save(self, deliveryman):
        save_query = "INSERT INTO deliveryman (deliveryman_id, name, email) VALUES (?, ?, ?)"
        save_params = (deliveryman.deliveryman_id, deliveryman.name, deliveryman.email)

        self.execute_query_one(save_query, save_params)
        self.commit()
