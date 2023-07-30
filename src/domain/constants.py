CONFIG_PATH = "src/infrastructure/config/"
DELIVERY_STATUS = ['accepted', 'preparing', 'available for delivery', 'delivering', 'delivered']

# BD
STORAGE_TYPE = "mysql"
STORAGE_SQLITE_NAME = "ifome.db"
STORAGE_SQLITE_PATH = f"{CONFIG_PATH}{STORAGE_SQLITE_NAME}"

# MESSAGE_BROKER
DELIVERY_QUEUE = "delivery"
STATUS_QUEUE = "status"
MESSAGE_BROKER_TYPE = "rabbitmq"
HOST_MESSAGE_BROKER = "localhost"
