from src.domain.interfaces.deliveryman_interface import DeliverymanStorage
from src.domain.models.deliveryman_model import DeliverymanModel
from src.exceptions.custom_exceptions import NotFoundFail
from src.infrastructure.config.config_storage import ConfigStorage
from src.infrastructure.service.mysql import MySQL


class DeliverymanStorageMySQL(MySQL, DeliverymanStorage):
    def __init__(self):
        super(DeliverymanStorageMySQL, self).__init__(ConfigStorage)
        self.create_table()

    def create_table(self):
        create_table_query = (
            "CREATE TABLE IF NOT EXISTS deliverymans ("
            "deliveryman_id VARCHAR(36) PRIMARY KEY,"
            "name VARCHAR(255) NOT NULL,"
            "email VARCHAR(255) NOT NULL,"
            "available BOOLEAN NOT NULL DEFAULT TRUE"
            ")"
        )

        self.execute_query_one(create_table_query)
        self.commit()

    def get_all(self):
        get_all_query = "SELECT * FROM deliverymans"

        if deliverymans := self.execute_query_many(get_all_query):
            return [DeliverymanModel(*deliveryman) for deliveryman in deliverymans]
        else:
            raise NotFoundFail('Deliveryman not found')

    def get_by_id(self, value_id, key_id="deliveryman_id", return_fields="*"):
        get_by_id_query = f"SELECT {return_fields} FROM deliverymans WHERE {key_id} = %s"
        get_by_id_params = (value_id,)
        data_deliveryman = self.execute_query_one(get_by_id_query, get_by_id_params)

        if data_deliveryman and return_fields == "*":
            return DeliverymanModel(*data_deliveryman)
        elif data_deliveryman and return_fields != "*":
            return data_deliveryman
        else:
            raise NotFoundFail('Deliveryman not found')

    def save(self, deliveryman: DeliverymanModel):
        save_query = "INSERT INTO deliverymans (deliveryman_id, name, email, available) VALUES (%s, %s, %s, %s)"
        save_params = (deliveryman.deliveryman_id, deliveryman.name, deliveryman.email, deliveryman.available)

        self.execute_query_one(save_query, save_params)
        self.commit()
        self.connection_close()
