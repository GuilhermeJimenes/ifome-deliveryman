class StatusMessageBroker:
    def change_status(self, message):
        raise NotImplementedError()

    def view_status(self):
        raise NotImplementedError()

    def connection_close(self):
        raise NotImplementedError()
