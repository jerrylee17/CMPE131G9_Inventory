from flask import Flask

app = Flask(__name__)

from app import MainPage
from app import DeliveredPage
from app import LoginPage