import pytest
from app.Pages import Stock
from app.Pages.models import ingredientInventory,dishIngredientReq,disposalRecord
from flask import render_template,request, redirect, Flask, current_app

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asd'

@pytest.fixture(scope='module')
def get_use_dish():
    with app.app_context():
        with app.test_request_context():
            form = Stock.usingDish()
            return form

def test_use_dish(get_use_dish):
    with app.app_context():
        with app.test_request_context():
            assert get_use_dish.dishIngredients == dishIngredientReq.query.all()