from src.domain.interfaces.deliveryman_interface import DeliverymanStorage
from src.domain.interfaces.delivery_interface import DeliveryStorage
from src.domain.interfaces.status_interface import StatusMessageBroker


class StatusCore:
    def __init__(self, deliveryman_storage: DeliverymanStorage, deliveries_storage: DeliveryStorage,
                 status_message_broker: StatusMessageBroker):
        self.deliveryman_storage = deliveryman_storage
        self.deliveries_storage = deliveries_storage
        self.status_message_broker = status_message_broker

    def get_delivery(self, delivery_id):
        if delivery_id:
            return self.deliveries_storage.get_by_id(delivery_id)
        else:
            print('delivery_id:', delivery_id)

    def change_deliveryman_availability(self, deliveryman_id, new_status):
        available = True if new_status == 'delivered' else False
        self.deliveryman_storage.update(deliveryman_id, available)

    def update_delivery_status(self, delivery, delivery_id, new_status):
        delivery.status = new_status
        self.deliveries_storage.update(delivery_id, new_status)
        return delivery

    def send_delivery_status(self, new_status):
        self.status_message_broker.publish_status(new_status)
        self.status_message_broker.close_connection()

    def change_status(self, delivery_id, new_status):
        delivery = self.get_delivery(delivery_id)
        self.change_deliveryman_availability(delivery.deliveryman_id, new_status)
        delivery = self.update_delivery_status(delivery, delivery_id, new_status)
        self.send_delivery_status(new_status)
        return delivery

