from flask_restx import Namespace, fields

# Namespaces
deliveryman_ns = Namespace('user')

# Payloads
create_deliveryman_payload = deliveryman_ns.model('CreateDeliverymanPayload', {
    'name': fields.String(required=True),
    'email': fields.String(required=True)
}, strict=True)

# Headers
