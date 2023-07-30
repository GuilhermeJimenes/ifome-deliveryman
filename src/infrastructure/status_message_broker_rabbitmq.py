from src.domain.constants import STATUS_QUEUE
from src.domain.interfaces.status_interface import StatusMessageBroker
from src.infrastructure.service.rabbitmq import RabbitMQ


class StatusMessageBrokerRabbitMQ(RabbitMQ, StatusMessageBroker):
    def publish_status(self, message):
        self.new_queue(STATUS_QUEUE)
        self.publish(STATUS_QUEUE, message)

