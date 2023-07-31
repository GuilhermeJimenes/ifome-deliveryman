class DeliverymanStorage:
    def create_table(self):
        raise NotImplementedError()

    def get_all(self):
        raise NotImplementedError()

    def save(self, deliveryman):
        raise NotImplementedError()

    def update(self, deliveryman_id, new_available):
        raise NotImplementedError()

    def get_by_id(self, value_id, key_id="deliveryman_id", return_fields="*"):
        raise NotImplementedError()
