from dataclasses import dataclass


@dataclass
class DeliverymanModel:
    deliveryman_id: str
    name: str
    email: str
    available: str = True
