from src.domain.interfaces.user_interface import UserStorage
from src.domain.interfaces.status_interface import StatusMessageBroker
from src.domain.models.user_model import UserModel
from src.exceptions.custom_exceptions import InvalidInputFail
from src.utils.email import is_valid_email
from src.utils.parser import create_hash


class GetAllUsersCore:
    def __init__(self, user_storage: UserStorage):
        self.user_storage = user_storage

    def get_all_users(self):
        return self.user_storage.get_all()


class GetUserByIdCore:
    def __init__(self, user_storage: UserStorage):
        self.user_storage = user_storage

    def get_user_by_id(self, user_id):
        return self.user_storage.get_by_id(user_id)


class CreateUserCore:
    def __init__(self, user_storage: UserStorage):
        self.user_storage = user_storage

    def validate_user_credential(self, email):
        if not is_valid_email(email):
            raise InvalidInputFail("Invalid email.")

    def new_user(self, name, email):
        user_id = create_hash(email)
        return UserModel(user_id, name, email)

    def create_user(self, name, email):
        self.validate_user_credential(email)
        user = self.new_user(name, email)
        self.user_storage.save(user)
        return user
