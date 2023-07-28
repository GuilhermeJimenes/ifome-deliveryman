from src.domain.interfaces.deliveryman_interface import DeliverymanStorage
from src.domain.interfaces.status_interface import StatusMessageBroker
from src.domain.models.deliveryman_model import DeliverymanModel
from src.exceptions.custom_exceptions import InvalidInputFail
from src.utils.email import is_valid_email
from src.utils.parser import create_hash


class GetAllDeliverymansCore:
    def __init__(self, deliveryman_storage: DeliverymanStorage):
        self.deliveryman_storage = deliveryman_storage

    def get_all_deliverymans(self):
        return self.deliveryman_storage.get_all()


class GetDeliverymanByIdCore:
    def __init__(self, deliveryman_storage: DeliverymanStorage):
        self.deliveryman_storage = deliveryman_storage

    def get_deliveryman_by_id(self, deliveryman_id):
        return self.deliveryman_storage.get_by_id(deliveryman_id)


class CreateDeliverymanCore:
    def __init__(self, deliveryman_storage: DeliverymanStorage):
        self.deliveryman_storage = deliveryman_storage

    def validate_deliveryman_credential(self, email):
        if not is_valid_email(email):
            raise InvalidInputFail("Invalid email.")

    def new_deliveryman(self, name, email):
        deliveryman_id = create_hash(email)
        return DeliverymanModel(deliveryman_id, name, email)

    def create_deliveryman(self, name, email):
        self.validate_deliveryman_credential(email)
        deliveryman = self.new_deliveryman(name, email)
        self.deliveryman_storage.save(deliveryman)
        return deliveryman
