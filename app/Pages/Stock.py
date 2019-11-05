from app import app
from flask import render_template,request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField
from app.obj.User import User
from wtforms.validators import DataRequired
import os
from app.Pages.models import ingredientInventory,dishIngredientReq
from app import db

app.config['SECRET_KEY'] = 'some-key'
'''
inventory = ingredientInventory.query.all()

for i in inventory:
    print(i.id,i.ingredientName,i.quantity,i.unitMeasure)'''

'''
dishIngredients = dishIngredientReq.query.all()

for i in dishIngredients:
    print(i.id,i.dishName,i.ingredientName2,i.quantity2,i.unitMeasure2)'''

@app.route('/stock',methods = ["GET","POST"])

def stock():

    form = checkForm()

    if form.validate_on_submit():

        if form.submit1.data:
            return redirect("/checkStockByDish")
        elif form.submit2.data:
            return redirect("/checkStockByIngredient")

    return render_template('stock.html',form=form)

@app.route('/checkStockByDish',methods = ["GET","POST"])

def byDish():

    form2 = usingDish()

    return render_template('checkStockByDish.html',form2=form2)

@app.route('/checkStockByIngredient',methods = ["GET","POST"])

def byIngredient():

    form3 = usingIngredient()

    return render_template('checkStockByIngredient.html',form3=form3)

class checkForm(FlaskForm):

    submit1 = SubmitField("By Dish")
    submit2 = SubmitField("By Ingredient")

class usingDish(FlaskForm):

    dishIngredients = dishIngredientReq.query.all()

    mainList=[]

    for item in dishIngredients:
    
        mainList.append(item.dishName)

    noDuplicateList = list(set(mainList))

    noDuplicateList.sort()

    pairs=[]

    for item2 in noDuplicateList:

        pairs.append([item2,item2])

    dish = SelectField(u'Dishes', choices=pairs)

    submit3 = SubmitField('GO')

class usingIngredient(FlaskForm):

    inventoryTemp = ingredientInventory.query.all()

    generalList=[]

    for item in inventoryTemp:
    
        object1 = item.ingredientName
        object2 = item.ingredientName

        generalList.append([object1,object2])

    ingredient = SelectField(u'Ingredients', choices=generalList)

    submit4 = SubmitField('GO')

if __name__ == '__main__':
    app.run(debug=True)