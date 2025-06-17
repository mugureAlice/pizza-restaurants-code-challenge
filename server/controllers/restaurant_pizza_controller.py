from flask import Blueprint, make_response, request
from server.models.restaurant_pizza import RestaurantPizza
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server import db

restaurant_pizzas_bp = Blueprint('restaurant_pizzas', __name__)

@restaurant_pizzas_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()

   
    required_fields = ["price", "pizza_id", "restaurant_id"]
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        return make_response(
            {"errors": [f"Missing required fields: {', '.join(missing_fields)}"]},
            400
        )

   
    if not isinstance(data["price"], int) or not (1 <= data["price"] <= 30):
        return make_response(
            {"errors": ["Price must be an integer between 1 and 30"]},
            400
        )

    
    restaurant = Restaurant.query.get(data["restaurant_id"])
    pizza = Pizza.query.get(data["pizza_id"])

    if not restaurant:
        return make_response({"errors": ["Restaurant not found"]}, 404)
    if not pizza:
        return make_response({"errors": ["Pizza not found"]}, 404)

   
    restaurant_pizza = RestaurantPizza(
        price=data["price"],
        pizza_id=data["pizza_id"],
        restaurant_id=data["restaurant_id"]
    )

    db.session.add(restaurant_pizza)
    db.session.commit()

    return make_response(restaurant_pizza.to_dict(), 201)