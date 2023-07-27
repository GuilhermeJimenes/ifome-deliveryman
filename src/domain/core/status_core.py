from src.domain.interfaces.status_interface import StatusMessageBroker


class StatusCore:
    def __init__(self, status_message_broker: StatusMessageBroker):
        self.status_message_broker = status_message_broker

    def change_status(self, _id, new_status):
        self.status_message_broker.change_status(new_status)
        self.status_message_broker.connection_close()
