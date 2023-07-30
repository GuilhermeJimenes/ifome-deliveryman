from src.domain.constants import MESSAGE_BROKER_TYPE, STORAGE_TYPE
from src.domain.core.delivery_core import DeliveryCore
from src.domain.interfaces.delivery_interface import DeliveryStorage, DeliveryMessageBroker
from src.exceptions.custom_exceptions import NotFoundFail, RabbitMQError
from src.infrastructure.delivery_storage_mysql import DeliveryStorageMySQL
from src.infrastructure.delivery_storage_sqlite import DeliveryStorageSQLite
from src.infrastructure.delivery_message_broker_rabbitmq import DeliveryMessageBrokerRabbitMQ


class DeliveryApp:
    def __init__(self):
        if STORAGE_TYPE == "mysql":
            self.deliveries_storage: DeliveryStorage = DeliveryStorageMySQL()
        elif STORAGE_TYPE == "sqlite":
            self.deliveries_storage: DeliveryStorage = DeliveryStorageSQLite()
        else:
            raise ValueError("Invalid storage, valid types: sqlite, mysql")

        if MESSAGE_BROKER_TYPE == "rabbitmq":
            self.delivery_message_broker: DeliveryMessageBroker = DeliveryMessageBrokerRabbitMQ()
        else:
            raise ValueError("Invalid message broker, valid types: rabbitmq")

    def delivery(self):
        try:
            delivery_core = DeliveryCore(self.deliveries_storage, self.delivery_message_broker)
            response = delivery_core.delivery().__dict__
            self.delivery_message_broker.consume_success()
            return response
        except NotFoundFail as error:
            print(error)
            self.delivery_message_broker.close_connection()
            return 'error'
        except KeyboardInterrupt as error:
            print(error)
            self.delivery_message_broker.close_connection()
            return 'error'
        except RabbitMQError as error:
            print(error)
            self.delivery_message_broker.close_connection()
            return 'error'
