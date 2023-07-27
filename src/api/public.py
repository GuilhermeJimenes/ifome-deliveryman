from flask import Flask
from flask_cors import CORS
from flask_restx import Api

from src.presentation.payloads.status import status_ns
from src.presentation.payloads.user import user_ns
from src.presentation.resources.status import Status
from src.presentation.resources.user import Users, User

print('public')

# configs
app = Flask(__name__)
cors = CORS(app)
api = Api(app)

# namespaces
api.add_namespace(user_ns)
api.add_namespace(status_ns)

# resources
user_ns.add_resource(Users, '')
user_ns.add_resource(User, '/<string:_id>')
status_ns.add_resource(Status, '/<string:_id>')
