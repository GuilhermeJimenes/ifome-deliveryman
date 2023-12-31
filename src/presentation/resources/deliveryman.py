from flask import request
from flask_restx import Resource

from src.application.deliveryman_app import DeliverymanApp
from src.presentation.payloads.deliveryman import deliveryman_ns, create_deliveryman_payload


class Deliverymans(Resource):
    def get(self):
        """Lista todos os entregadores"""
        response = DeliverymanApp().get_all_deliverymans()
        return response

    @deliveryman_ns.expect(create_deliveryman_payload, validate=True)
    def post(self):
        """Registra um novo entregador"""
        data = request.get_json()

        response = DeliverymanApp().create_deliveryman(data['name'], data['email'])
        return response


class Deliveryman(Resource):
    """Lista um único entregador, buscando pelo seu id"""
    def get(self, _id):
        response = DeliverymanApp().get_deliveryman_by_id(_id)
        return response
