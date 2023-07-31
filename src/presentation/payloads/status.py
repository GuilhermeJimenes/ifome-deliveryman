from flask_restx import Namespace, fields

from src.domain.constants import DELIVERY_STATUS

# Namespaces
status_ns = Namespace("status")

# Payloads
change_status_payload = status_ns.model("ChangeStatusPayload", {
    "new_status": fields.String(required=True, enum=DELIVERY_STATUS)
}, strict=True)

# Headers
