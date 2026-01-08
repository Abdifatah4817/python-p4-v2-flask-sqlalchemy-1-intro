from flask import Flask
from flask_migrate import Migrate
from models import db

# create the Flask app
app = Flask(__name__)

# configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# initialize SQLAlchemy with the app
db.init_app(app)

# initialize Flask-Migrate
migrate = Migrate(app, db)

# test route
@app.route('/')
def index():
    return "<h1>Flask + SQLAlchemy is working!</h1>"

if __name__ == '__main__':
    app.run(port=5555, debug=True)
