from src.api.http.http_response import HttpResponse
from src.domain.constants import STORAGE_TYPE, MESSAGE_BROKER_TYPE
from src.domain.core.status_core import StatusCore
from src.domain.interfaces.delivery_interface import DeliveryStorage
from src.domain.interfaces.status_interface import StatusMessageBroker
from src.domain.interfaces.deliveryman_interface import DeliverymanStorage
from src.exceptions.custom_exceptions import RabbitMQError
from src.infrastructure.delivery_storage_mysql import DeliveryStorageMySQL
from src.infrastructure.delivery_storage_sqlite import DeliveryStorageSQLite
from src.infrastructure.status_message_broker_rabbitmq import StatusMessageBrokerRabbitMQ
from src.infrastructure.deliveryman_storage_mysql import DeliverymanStorageMySQL
from src.infrastructure.deliveryman_storage_sqlite import DeliverymanStorageSQLite


class StatusApp:
    def __init__(self):
        if STORAGE_TYPE == "mysql":
            self.deliveryman_storage: DeliverymanStorage = DeliverymanStorageMySQL()
            self.deliveries_storage: DeliveryStorage = DeliveryStorageMySQL()
        elif STORAGE_TYPE == "sqlite":
            self.deliveryman_storage: DeliverymanStorage = DeliverymanStorageSQLite()
            self.deliveries_storage: DeliveryStorage = DeliveryStorageSQLite()
        else:
            raise ValueError("Invalid storage, valid types: sqlite, mysql")

        if MESSAGE_BROKER_TYPE == "rabbitmq":
            self.status_message_broker: StatusMessageBroker = StatusMessageBrokerRabbitMQ()
        else:
            raise ValueError("Invalid message broker, valid types: rabbitmq")

    def change_status(self, delivery_id, new_status):
        try:
            status_core = StatusCore(self.deliveryman_storage, self.deliveries_storage, self.status_message_broker)
            response = status_core.change_status(delivery_id, new_status)
            return HttpResponse.success('Status changed successfully!', response.__dict__)
        except RabbitMQError as error:
            return HttpResponse.internal_error(message=str(error))
