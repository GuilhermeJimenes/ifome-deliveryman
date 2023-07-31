class DeliveryStorage:
    def create_table(self):
        raise NotImplementedError()

    def get_by_id(self, client_id, return_fields="*"):
        raise NotImplementedError()

    def update(self, delivery_id, new_status):
        raise NotImplementedError()

    def save(self, delivery):
        raise NotImplementedError()


class DeliveryMessageBroker:
    def consume_delivery(self):
        raise NotImplementedError()

    def consume_success(self):
        raise NotImplementedError()

    def close_connection(self):
        raise NotImplementedError()
