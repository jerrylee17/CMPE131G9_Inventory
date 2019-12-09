from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__,static_url_path="/app/templates/static")
app.config.from_object(Config)

db = SQLAlchemy(app)

login = LoginManager(app)

from app.Pages import Input
from app.Pages import Dispose
from app.Pages import FoodOrder
from app.Pages import Login
from app.Pages import Main
from app.Pages import MakeMenu
from app.Pages import Manage
from app.Pages import Registration
from app.Pages import Stock
from app.Pages import models
from app.Pages import Fullmenu