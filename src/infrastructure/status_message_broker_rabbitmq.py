from src.domain.constants import DELIVERY_QUEUE_NAME
from src.domain.interfaces.status_interface import StatusMessageBroker
from src.infrastructure.service.rabbitmq import RabbitMQ


class StatusMessageBrokerRabbitMQ(RabbitMQ, StatusMessageBroker):
    queue_name = DELIVERY_QUEUE_NAME

    def change_status(self, message):
        self.new_queue(self.queue_name)
        self.publish(self.queue_name, message)

    def view_status(self):
        self.new_queue(self.queue_name)
        self.consume(self.queue_name)

