from src.domain.interfaces.delivery_interface import DeliveryStorage, DeliveryMessageBroker


class DeliveryCore:
    def __init__(self, deliveries_storage: DeliveryStorage, delivery_message_broker: DeliveryMessageBroker):
        self.deliveries_storage = deliveries_storage
        self.delivery_message_broker = delivery_message_broker

    def get_delivery_id(self):
        return self.delivery_message_broker.consume_delivery()

    def get_delivery(self, delivery_id):
        if delivery_id:
            return self.deliveries_storage.get_by_id(delivery_id)

    def delivery(self):
        delivery_id = self.get_delivery_id()
        delivery = self.get_delivery(delivery_id)
        return delivery
