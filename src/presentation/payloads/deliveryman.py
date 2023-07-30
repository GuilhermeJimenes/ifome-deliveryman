from flask_restx import Namespace, fields

# Namespaces
deliveryman_ns = Namespace("deliveryman")

# Payloads
create_deliveryman_payload = deliveryman_ns.model("CreateDeliverymanPayload", {
    "name": fields.String(required=True, example="Entregador"),
    "email": fields.String(required=True, example="Entregador@gmail.com")
}, strict=True)

# Headers
