from src.api.http.http_response import HttpResponse
from src.domain.core.status_core import StatusCore
from src.domain.interfaces.status_interface import StatusMessageBroker
# from src.domain.interfaces.user_interface import UserStorage
from src.exceptions.custom_exceptions import RabbitMQError
from src.infrastructure.status_message_broker_rabbitmq import StatusMessageBrokerRabbitMQ
# from src.infrastructure.user_storage_mysql import UserStorageMySQL
# from src.infrastructure.user_storage_sqlite import UserStorageSQLite


class StatusApp:
    def __init__(self):
        # self.user_storage: UserStorage = UserStorageSQLite()
        # self.user_storage: UserStorage = UserStorageMySQL()
        self.status_message_broker: StatusMessageBroker = StatusMessageBrokerRabbitMQ()

    def change_status(self, _id, new_status):
        try:
            status_use_cases = StatusCore(self.status_message_broker)
            response = status_use_cases.change_status(_id, new_status)
            return HttpResponse.success('Status changed successfully!', response)
        except RabbitMQError as error:
            return HttpResponse.internal_error(message=str(error))
