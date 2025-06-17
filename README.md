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

python server/seed.py