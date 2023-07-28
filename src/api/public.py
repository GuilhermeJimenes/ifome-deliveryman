from flask import Flask
from flask_cors import CORS
from flask_restx import Api

from src.presentation.payloads.status import status_ns
from src.presentation.payloads.deliveryman import deliveryman_ns
from src.presentation.resources.status import Status
from src.presentation.resources.deliveryman import Deliverymans, Deliveryman

print('public')

# configs
app = Flask(__name__)
cors = CORS(app)
api = Api(app)

# namespaces
api.add_namespace(deliveryman_ns)
api.add_namespace(status_ns)

# resources
deliveryman_ns.add_resource(Deliverymans, '')
deliveryman_ns.add_resource(Deliveryman, '/<string:_id>')
status_ns.add_resource(Status, '/<string:_id>')
