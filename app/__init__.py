from flask import Flask
from app.config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

signin = LoginManager(app)
signin.signin_view = "signin"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models