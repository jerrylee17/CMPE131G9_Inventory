import pytest
from app.Pages import Input
from flask import render_template,request, redirect, Flask, current_app
from app import db
from app.Pages.models import ingredientInventory

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asd'


def test_input():
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
            amountToBeAdded = 1000

            #create and fill out form
            form = Input.InputForm()
            form.isel.data = ingredientName
            form.quantity.data = amountToBeAdded

            #run the submission method
            Input.input2(form)

            finalQuantity = selectedIngredient.quantity
            
            selectedIngredient.quantity = initQuantity
            db.session.commit()

            assert finalQuantity == initQuantity+amountToBeAdded


