from src.api.http.http_response import HttpResponse
from src.domain.constants import STORAGE_TYPE
from src.domain.core.deliveryman_core import GetAllDeliverymansCore, GetDeliverymanByIdCore, CreateDeliverymanCore
from src.domain.interfaces.deliveryman_interface import DeliverymanStorage
from src.exceptions.custom_exceptions import NotFoundFail, InvalidInputFail, RabbitMQError
from src.infrastructure.deliveryman_storage_mysql import DeliverymanStorageMySQL
from src.infrastructure.deliveryman_storage_sqlite import DeliverymanStorageSQLite


class DeliverymanApp:
    def __init__(self):
        if STORAGE_TYPE == "mysql":
            self.deliveryman_storage: DeliverymanStorage = DeliverymanStorageMySQL()
        elif STORAGE_TYPE == "sqlite":
            self.deliveryman_storage: DeliverymanStorage = DeliverymanStorageSQLite()
        else:
            raise ValueError("Invalid storage, valid types: sqlite, mysql")

    def get_all_deliverymans(self):
        try:
            deliveryman_core = GetAllDeliverymansCore(self.deliveryman_storage)
            response = [deliveryman.__dict__ for deliveryman in deliveryman_core.get_all_deliverymans()]
            return HttpResponse.success('Deliverers successfully found!', response)
        except NotFoundFail as error:
            return HttpResponse.failed(message=str(error))

    def get_deliveryman_by_id(self, deliveryman_id):
        try:
            deliveryman_core = GetDeliverymanByIdCore(self.deliveryman_storage)
            response = deliveryman_core.get_deliveryman_by_id(deliveryman_id)
            return HttpResponse.success('Deliverer found successfully!', response.__dict__)
        except NotFoundFail as error:
            return HttpResponse.failed(message=str(error))

    def create_deliveryman(self, name, email):
        try:
            deliveryman_core = CreateDeliverymanCore(self.deliveryman_storage)
            response = deliveryman_core.create_deliveryman(name, email)
            return HttpResponse.success('Deliveryman created successfully', response.__dict__)
        except InvalidInputFail as error:
            return HttpResponse.failed(message=str(error))
        except RabbitMQError as error:
            return HttpResponse.internal_error(message=str(error))
