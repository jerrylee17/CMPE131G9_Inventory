import pytest
from app.Pages import Dispose
from flask import render_template,request, redirect, Flask, current_app
from app import db
from app.Pages.models import ingredientInventory

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asd'


def test_dispose():
    with app.app_context():
        with app.test_request_context():
            ingredientName = 'Angel Hair Pasta'
            idNumber = 0
            for i in ingredientInventory.query.all():
                if i.ingredientName == ingredientName:
                    idNumber = i.id
                    break
            selectedIngredient = ingredientInventory.query.get(idNumber)
            initQuantity = selectedIngredient.quantity
            amountToBeDisposed = 500

            #create and fill out form
            form = Dispose.disposal()
            form.ingredient.data = ingredientName
            form.quantity.data = amountToBeDisposed
            form.usercomment.data = 'dispose'

            #run the submission method
            Dispose.dispose2(form)

            finalQuantity = selectedIngredient.quantity

            selectedIngredient.quantity = initQuantity
            db.session.commit()

            assert finalQuantity == initQuantity-amountToBeDisposed


