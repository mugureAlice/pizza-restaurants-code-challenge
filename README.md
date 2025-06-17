<!--  Pizza Restaurant API -->

A RESTful API for a Pizza Restaurant built with Flask and SQLAlchemy.

<!-- Setup Instructions -->

1. Clone the repository:
   git clone https://github.com/your-username/pizza-api-challenge.git
   cd pizza-api-challenge

<!-- Create a virtual environment and install packages -->

pipenv install flask flask_sqlalchemy flask_migrate
pipenv shell

<!-- Run DB setup commands -->

export FLASK_APP=server/app.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

<!-- seed the database -->
python server/seed.py

 <!-- Route Summary -->

Method        Route                       Description    
GET           /restaurants                Get a list of all restaurants 
GET           /restaurants/<int:id>       Get details of a specific restaurant and its pizzas
DELETE        /restaurants/<int:id>       Delete a restaurant and its associated restaurant_pizzas
GET           /pizzas                     Get a list of all pizzas    
POST          /restaurant_pizzas          Create a new RestaurantPizza entry  

<!-- Example requests & responses for each route -->
http://localhost:5555/restaurants/1

<!-- How to use postman -->
Open Postman.
Click "Import" 
Upload the file: challenge-1-pizzas.postman_collection.json
Click “Import”
Go to the “Collections” tab 
Expand the Pizza API collection.
Click on any request
Make sure your Flask app is running 
Hit “Send” to test.

