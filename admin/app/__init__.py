
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_login import LoginManager
from flask_jwt_extended import JWTManager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
login_manager = LoginManager()
migrate = Migrate(app, db)
login_manager.init_app(app)
jwt = JWTManager(app)
PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER_IMG = '{}/static/img/'.format(PROJECT_HOME)
bootstrap = Bootstrap(app)

from app import routes, models