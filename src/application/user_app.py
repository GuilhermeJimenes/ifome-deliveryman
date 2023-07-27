from src.api.http.http_response import HttpResponse
from src.domain.core.user_core import GetAllUsersCore, GetUserByIdCore, CreateUserCore
from src.domain.interfaces.user_interface import UserStorage
from src.exceptions.custom_exceptions import NotFoundFail, InvalidInputFail, RabbitMQError
from src.infrastructure.user_storage_mysql import UserStorageMySQL
# from src.infrastructure.user_storage_sqlite import UserStorageSQLite


class UserApp:
    def __init__(self):
        # self.user_storage: UserStorage = UserStorageSQLite()
        self.user_storage: UserStorage = UserStorageMySQL()

    def get_all_users(self):
        try:
            user_use_cases = GetAllUsersCore(self.user_storage)
            response = [user.__dict__ for user in user_use_cases.get_all_users()]
            return HttpResponse.success('Deliverers successfully found!', response)
        except NotFoundFail as error:
            return HttpResponse.failed(message=str(error))

    def get_user_by_id(self, user_id):
        try:
            user_use_cases = GetUserByIdCore(self.user_storage)
            response = user_use_cases.get_user_by_id(user_id)
            return HttpResponse.success('Deliverer found successfully!', response.__dict__)
        except NotFoundFail as error:
            return HttpResponse.failed(message=str(error))

    def create_user(self, name, email):
        try:
            user_use_cases = CreateUserCore(self.user_storage)
            response = user_use_cases.create_user(name, email)
            return HttpResponse.success('User created successfully', response.__dict__)
        except InvalidInputFail as error:
            return HttpResponse.failed(message=str(error))
        except RabbitMQError as error:
            return HttpResponse.internal_error(message=str(error))
