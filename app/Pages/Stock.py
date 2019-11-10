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

'''selectedIngredient = ingredientInventory.query.get(1)

selectedIngredient.quantity = 4530.00
db.session.commit()'''
'''
inventory = ingredientInventory.query.all()

for i in inventory:
    print(i.id,i.ingredientName,i.quantity,i.unitMeasure)'''

'''
dishIngredients = dishIngredientReq.query.all()

for i in dishIngredients:
    print(i.id,i.dishName,i.ingredientName2,i.quantity2,i.unitMeasure2)'''


'''record = disposalRecord.query.all()

for i in record:
    print(i.id,i.userName,i.ingredientName3,i.quantity3,i.unitMeasure3,i.comment)'''

@app.route('/stock',methods = ["GET","POST"])
@login_required
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

    if form2.validate_on_submit():

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

        ing = []
        quan = []
        mea = []

        finalList = []

        temp = None

        signal = True

        for i in idList:
            for j in inventory:
                if i == j.id:
                    temp ="Product ID Number:"+str(i)+"| Ingredient:"+j.ingredientName+" Quantity:"+str(j.quantity)+j.unitMeasure
                    finalList.append(temp)
                    temp = None
                    ing.append(j.ingredientName)
                    quan.append(j.quantity)
                    mea.append(j.unitMeasure)
                    

        return render_template('checkStockByDish.html',form2=form2,signal=signal,finalList = finalList)
        
    return render_template('checkStockByDish.html',form2=form2)

@app.route('/checkStockByIngredient',methods = ["GET","POST"])

def byIngredient():

    form3 = usingIngredient()

    if form3.validate_on_submit():
        
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

        pairs.append([item2.replace(" ", "_"),item2])

    dish = SelectField(u'Dishes', choices=pairs)

    submit3 = SubmitField('GO')

class usingIngredient(FlaskForm):

    inventoryTemp = ingredientInventory.query.all()

    generalList=[]

    for item in inventoryTemp:
    
        object1 = item.ingredientName
        object2 = item.ingredientName

        generalList.append([object1.replace(" ", "_"),object2])

    ingredient = SelectField(u'Ingredients', choices=generalList)

    submit4 = SubmitField('GO')

if __name__ == '__main__':
    app.run(debug=True)