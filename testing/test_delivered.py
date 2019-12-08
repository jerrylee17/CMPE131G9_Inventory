import pytest
from app.Pages import Dispose
from flask import render_template,request, redirect, Flask, current_app
from app import db
from app.Pages.models import ingredientInventory

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asd'


def test_delivered():
    with app.app_context():
        with app.test_request_context():
            ingredientName = 'Baking Powder'
            idNumber = 0
            for i in ingredientInventory.query.all():
                if i.ingredientName == ingredientName:
                    idNumber = i.id
                    break
            selectedIngredient = ingredientInventory.query.get(idNumber)
            initQuantity = selectedIngredient.quantity
            amountToBeAdded = 500

            #create and fill out form
            form = Delivered.de
            form.submit()
            form.ingredient.data = 'Angel Hair Pasta'
            form.quantity.data = amountToBeAdded
            form.usercomment.data = 'dispose'

            #run the submission method
            Dispose.dispose2(form)

            finalQuantity = selectedIngredient.quantity
            
            selectedIngredient.quantity = initQuantity
            db.session.commit()

            assert finalQuantity == initQuantity-amountToBeAdded


