from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from config import Config

# Flask
app = Flask(__name__)
app.config.from_object(Config)

# Flask-SQLAlchemy
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Flask-login
login = LoginManager(app)
login.login_view = 'view_signin'

from app import routes
from app import models
from app import forms

