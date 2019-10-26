from flask import Flask

app = Flask(__name__,static_url_path="/app/templates/static")

from app import MainPage
from app import DeliveredPage
from app import LoginPage
from app import Register
from app import FoodOrder