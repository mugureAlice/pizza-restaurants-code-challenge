from flask import Blueprint, make_response
from server.models.pizza import Pizza

pizzas_bp = Blueprint('pizzas', __name__)

@pizzas_bp.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return make_response([pizza.to_dict() for pizza in pizzas])