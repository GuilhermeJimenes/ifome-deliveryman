from src.domain.constants import DELIVERY_QUEUE, STATUS_QUEUE
from src.domain.interfaces.delivery_interface import DeliveryMessageBroker
from src.infrastructure.service.rabbitmq import RabbitMQ


class DeliveryMessageBrokerRabbitMQ(RabbitMQ, DeliveryMessageBroker):
    def consume_delivery(self):
        return self.start_consuming(DELIVERY_QUEUE)
