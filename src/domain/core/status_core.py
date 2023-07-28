from src.domain.interfaces.deliveryman_interface import DeliverymanStorage
from src.domain.interfaces.deliveries_interface import DeliveriesStorage
from src.domain.interfaces.status_interface import StatusMessageBroker


class StatusCore:
    def __init__(self, deliveryman_storage: DeliverymanStorage, deliveries_storage: DeliveriesStorage, status_message_broker: StatusMessageBroker):
        self.deliveryman_storage = deliveryman_storage
        self.deliveries_storage = deliveries_storage
        self.status_message_broker = status_message_broker

    def get_delivery(self, delivery_id):
        return self.deliveries_storage.get_by_id(delivery_id)

    def get_deliveryman(self, deliveryman_id):
        return self.deliveryman_storage.get_by_id(deliveryman_id, key_id='deliveryman_id')

    def change_availability(self, deliveryman_id, new_status):
        deliveryman = self.get_deliveryman(deliveryman_id)
        deliveryman.available = True if new_status == 'delivered' else False

    def save_status(self, delivery, new_status):
        delivery.status = new_status
        self.deliveries_storage.save(delivery)

    def send_status(self, new_status):
        self.status_message_broker.change_status(new_status)
        self.status_message_broker.connection_close()

    def change_status(self, delivery_id, new_status):
        delivery = self.get_delivery(delivery_id)
        self.change_availability(delivery.deliveryman_id, new_status)
        self.save_status(delivery, new_status)
        self.send_status(new_status)

