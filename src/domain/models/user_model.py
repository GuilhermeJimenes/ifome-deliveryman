from dataclasses import dataclass


@dataclass
class UserModel:
    user_id: str
    name: str
    email: str
