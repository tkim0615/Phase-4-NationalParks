from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS

from models import db # disallows circular importing

# creates Flask app and sets up connection to park_visits DB
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///park_visits.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

# allows for schema migrations
migrate = Migrate(app, db)

db.init_app(app)

CORS(app) # necessary for client-side to server-side proxy routing