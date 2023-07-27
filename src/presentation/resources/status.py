from flask import request
from flask_restx import Resource

from src.application.status_app import StatusApp
from src.presentation.payloads.status import status_ns, change_status_payload


class Status(Resource):
    @status_ns.expect(change_status_payload, validate=True)
    def post(self, _id):
        data = request.get_json()

        response = StatusApp().change_status(_id, data['new_status'])
        return response
