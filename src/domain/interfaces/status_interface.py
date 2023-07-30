class StatusMessageBroker:
    def publish_status(self, message):
        raise NotImplementedError()

    def close_connection(self):
        raise NotImplementedError()
