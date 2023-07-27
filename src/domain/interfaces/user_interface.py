class UserStorage:
    def create_table(self):
        raise NotImplementedError()

    def get_all(self):
        raise NotImplementedError()

    def save(self, user):
        raise NotImplementedError()

    def get_by_id(self, user_id):
        raise NotImplementedError()
