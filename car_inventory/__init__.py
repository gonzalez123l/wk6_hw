from flask import Flask
from .api.routes import api
from .site.routes import site
from .authentication.routes import auth
from config import Config
from car_inventory.helpers import CustomJSONEncoder

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .models import db as root_db, login_manager, ma

# Import for Flask-Marshmallow
from flask_marshmallow import Marshmallow

from flask_cors import CORS


app = Flask(__name__)



app.register_blueprint(api)
app.register_blueprint(site)
app.register_blueprint(auth)

app.config.from_object(Config)

root_db.init_app(app)

migrate = Migrate(app,root_db)

login_manager.init_app(app)
login_manager.login_view = 'auth.signin' # Specify what page to load for NON-AUTHED users

app.json_encoder = CustomJSONEncoder

ma.init_app(app)


CORS(app)

