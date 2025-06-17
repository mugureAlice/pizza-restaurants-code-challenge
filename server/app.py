from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from server.config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    from server.models.restaurant import Restaurant
    from server.models.pizza import Pizza
    from server.models.restaurant_pizza import RestaurantPizza
    
    from server.controllers.restaurant_controller import restaurants_bp
    from server.controllers.pizza_controller import pizzas_bp
    from server.controllers.restaurant_pizza_controller import restaurant_pizzas_bp
    
    app.register_blueprint(restaurants_bp)
    app.register_blueprint(pizzas_bp)
    app.register_blueprint(restaurant_pizzas_bp)
    
    return app