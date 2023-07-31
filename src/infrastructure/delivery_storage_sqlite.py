from src.domain.constants import STORAGE_SQLITE_PATH
from src.domain.interfaces.delivery_interface import DeliveryStorage
from src.domain.models.delivery_model import DeliveryModel
from src.exceptions.custom_exceptions import NotFoundFail
from src.infrastructure.service.sqlite import SQLite


class DeliveryStorageSQLite(SQLite, DeliveryStorage):
    def __init__(self):
        super(DeliveryStorageSQLite, self).__init__(STORAGE_SQLITE_PATH)
        self.create_table()

    def create_table(self):
        create_table_query = (
            "CREATE TABLE IF NOT EXISTS deliveries ("
            "delivery_id TEXT PRIMARY KEY,"
            "client_id TEXT PRIMARY KEY,"
            "food_name TEXT NOT NULL,"
            "address TEXT NOT NULL"
            ")"
        )

        self.execute_query_one(create_table_query)

    def get_by_id(self, delivery_id, return_fields="*"):
        get_by_id_query = f"SELECT {return_fields} FROM deliveries WHERE delivery_id = ?"
        get_by_id_params = (delivery_id,)

        data_client = self.execute_query_one(get_by_id_query, get_by_id_params)

        if data_client and return_fields == "*":
            return DeliveryModel(*data_client)
        elif data_client and return_fields != "*":
            return data_client
        else:
            raise NotFoundFail('Delivery not found')

    def update(self, delivery_id, new_status):
        update_query = "UPDATE deliveries SET status = %s WHERE delivery_id = %s"
        update_params = (new_status, delivery_id)

        self.execute_query_one(update_query, update_params)
        self.commit()

    def save(self, delivery: DeliveryModel):
        save_query = "INSERT INTO deliveries (delivery_id, client_id, name, address) VALUES (?, ?, ?, ?)"
        save_params = (delivery.delivery_id, delivery.client_id, delivery.food_name, delivery.address)

        self.execute_query_one(save_query, save_params)
        self.commit()
