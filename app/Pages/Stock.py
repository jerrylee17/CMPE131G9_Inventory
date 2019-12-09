from app import app
from flask import render_template,request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField
from app.obj.User import User
from wtforms.validators import DataRequired
import os
from app.Pages.models import ingredientInventory,dishIngredientReq,disposalRecord
from app import db
from flask_login import login_required

app.config['SECRET_KEY'] = 'some-key'

def DgetChoices():
    """
    Get updated list of dishes

    Returns:
        List of tuples for a selectfield of dishes
    """
    dishIngredients = dishIngredientReq.query.all()
    mainList=[]
    for item in dishIngredients:
        mainList.append(item.dishName)
    noDuplicateList = list(set(mainList))
    noDuplicateList.sort()
    pairs=[]
    for item2 in noDuplicateList:
        pairs.append([item2.replace(" ", "_"),item2])
    return pairs

def IgetChoices():
    """
    Get updated list of ingredients

    Returns:
        List of tuples for a selectfield with updated ingredients
    """
    inventoryTemp = ingredientInventory.query.all()
    generalList=[]
    for item in inventoryTemp:
        object1 = item.ingredientName
        object2 = item.ingredientName
        generalList.append([object1.replace(" ", "_"),object2])
    generalList.sort(key=lambda x: x[0])
    return generalList

@app.route('/stock',methods = ["GET","POST"])
@login_required
def stock():
    """
    Stock page
    """
    form = checkForm()
    if form.validate_on_submit():
        if form.submit1.data:
            return redirect("/checkStockByDish")
        elif form.submit2.data:
            return redirect("/checkStockByIngredient")

    return render_template('stock.html',form=form)

@app.route('/checkStockByDish',methods = ["GET","POST"])
def byDish():
    """
    Check stock by dish page
    """
    form2 = usingDish()
    form2.dish.choices = DgetChoices()
    if form2.validate_on_submit():
        if form2.back.data:
            return redirect('/stock')
        ingredientList=[]
        dishIngre = dishIngredientReq.query.all()
        '''for i in dishIngre:
            print(i.id,i.dishName,i.ingredientName2,i.quantity2,i.unitMeasure2)'''
        for i in dishIngre:
            if i.dishName == form2.dish.data.replace("_", " "):
                ingredientList.append(i.ingredientName2)
        inventory = ingredientInventory.query.all()
        idList = []
        for i in ingredientList:
            for j in inventory:
                if i == j.ingredientName:
                    idList.append(j.id)
        
        idList.sort()
        # ing, quan, mea, finalList = [], [], [], []
        signal = True
        temp = []
        for i in idList:
            for j in inventory:
                if i == j.id:
                    temp.append([str(i), j.ingredientName,str(j.quantity), j.unitMeasure])
                    # temp ="Product ID Number:"+str(i)+"| Ingredient:"+j.ingredientName+" Quantity:"+str(j.quantity)+j.unitMeasure
                    # finalList.append(temp)
                    # temp = None
                    # ing.append(j.ingredientName)
                    # quan.append(j.quantity)
                    # mea.append(j.unitMeasure)
        # print(temp)
        return render_template('checkStockByDish.html',form2=form2,signal=signal,finalList = temp)
    return render_template('checkStockByDish.html',form2=form2)

@app.route('/checkStockByIngredient',methods = ["GET","POST"])
def byIngredient():
    """
    Check stock by ingredient page
    """
    form3 = usingIngredient()
    form3.ingredient.choices = IgetChoices()
    if form3.validate_on_submit():
        if form3.back.data:
            return redirect('stock')
        selected = form3.ingredient.data.replace("_", " ")
        inventory = ingredientInventory.query.all()
        for i in inventory:
            if i.ingredientName == selected:
                item1 = str(i.id)
                item2 = i.ingredientName
                item3 = str(i.quantity)+" "+str(i.unitMeasure)
                #return "ID Number:"+str(i.id)+"  Ingredient Name:"+i.ingredientName+ "  Quantity:"+str(i.quantity)+" "+str(i.unitMeasure)
                return render_template('checkStockByIngredient.html',form3=form3,item1=item1,item2=item2,item3=item3)
                break
    return render_template('checkStockByIngredient.html',form3=form3)

class checkForm(FlaskForm):
    """
    Initial stock form

    Selects dish or ingredient
    """
    submit1 = SubmitField("By Dish")
    submit2 = SubmitField("By Ingredient")

class usingDish(FlaskForm):
    """
    Using dish form
    """
    dishIngredients = dishIngredientReq.query.all()
    mainList=[]
    for item in dishIngredients:
        mainList.append(item.dishName)
    noDuplicateList = list(set(mainList))
    noDuplicateList.sort()
    pairs=[]
    for item2 in noDuplicateList:
        pairs.append([item2.replace(" ", "_"),item2])
    dish = SelectField(u'Dishes', choices=pairs)
    submit3 = SubmitField('Check!')
    back = SubmitField('Back to Stock')

class usingIngredient(FlaskForm):
    """
    Using ingredient form
    """
    inventoryTemp = ingredientInventory.query.all()
    generalList=[]
    for item in inventoryTemp:
        object1 = item.ingredientName
        object2 = item.ingredientName
        generalList.append([object1.replace(" ", "_"),object2])
    ingredient = SelectField(u'Ingredients', choices=generalList)
    submit4 = SubmitField('Check!')
    back = SubmitField('Back to Stock')

# if __name__ == '__main__':
#     app.run(debug=True)