from flask_restx import Namespace, fields

# Namespaces
user_ns = Namespace('user')

# Payloads
create_deliveryman_payload = user_ns.model('CreateDeliverymanPayload', {
    'name': fields.String(required=True),
    'email': fields.String(required=True)
}, strict=True)

# Headers
