from app import app
from flask import render_template,request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField, FloatField
from app.obj.User import User
from wtforms.validators import DataRequired
import os
from app.Pages.models import ingredientInventory,disposalRecord
from app import db
from flask import flash, redirect, request
from flask_login import login_required

app.config['SECRET_KEY'] = 'some-key'

def getChoices():
    """ 
    Get updated list of ingredients
    
    Returns: 
        List of tuples for a selectfield with updated ingredients
    """
    inventoryTemp = ingredientInventory.query.all()
    generalList=[]
    object2 = ""
    for item in inventoryTemp:
        object1 = item.ingredientName
        object2 = item.unitMeasure
        finalstr = str(object1) + " ( " + str(object2) + " ) "
        generalList.append([object1.replace(" ", "_"), finalstr])
    return generalList

@app.route('/dispose',methods=["GET","POST"])
@login_required
def dispose():
    """ 
    Dispose ingredients page
    """
    
    form = disposal()
    form.ingredient.choices = getChoices()
    if form.validate_on_submit():
        dispose2(form)

    '''
    idNumber = 0
    for i in inventory:
        if i.ingredientName == selected:
            idNumber = i.id
            break
    selectedIngredient = ingredientInventory.query.get(idNumber)
    if form.quantity.data <= 0:
        flash("Please enter something above 0!")
        return redirect("/dispose")
    elif form.quantity.data>selectedIngredient.quantity:
        flash("Available stock is less than que quantity to be disposed")
        return redirect("/dispose")
    newQuantity = selectedIngredient.quantity - form.quantity.data
    selectedIngredient.quantity = newQuantity
    db.session.commit()
    temp = disposalRecord(userName = "Logged User",ingredientName3=selected,quantity3=form.quantity.data,unitMeasure3=form.object2,comment=form.usercomment.data)
    db.session.add(temp)
    db.session.commit()
    flash("Removal successfull")
    return redirect("/dispose")
    '''
        #elif(selectedIngredient.quantity != form.measure)
    return render_template('dispose.html',form=form)

def dispose2(form):
    """ 
    Handle the disposal form onclick

    Args: 
        form(FlaskForm): form with the information
    """

    ing = form.ingredient.data.replace("_", " ")
    inv = ingredientInventory.query.all()

    idNumber = 0
    for i in inv:
        if i.ingredientName == ing:
            idNumber = i.id
            break
    selectedIngredient = ingredientInventory.query.get(idNumber)
    if form.quantity.data <= 0:
        flash("Invalid quantity, please use a positive number")
        return redirect("/dispose")
    elif form.quantity.data>selectedIngredient.quantity:
        flash("Available stock is less than the quantity to be disposed")
        return redirect("/dispose")
    newQuantity = selectedIngredient.quantity - form.quantity.data
    selectedIngredient.quantity = newQuantity
    db.session.commit()
    temp = disposalRecord(userName = "Logged User",ingredientName3=ing,\
        quantity3=form.quantity.data,unitMeasure3=selectedIngredient.unitMeasure,comment=form.usercomment.data)
    db.session.add(temp)
    db.session.commit()
    flash("Removal successfull")
    return redirect("/dispose")

class disposal(FlaskForm):
    """
    Disposal form
    """

    inventoryTemp = ingredientInventory.query.all()
    generalList=[]
    object2 = ""
    for item in inventoryTemp:
        object1 = item.ingredientName
        object2 = item.unitMeasure
        finalstr = str(object1) + " ( " + str(object2) + " ) "
        generalList.append([object1.replace(" ", "_"), finalstr])
    ingredient = SelectField(u'Ingredient', choices=generalList)
    # measure = SelectField(u'Measure', choices=[('unit', 'unit'),('ml', 'ml'), ('gr', 'gr')])
    quantity = FloatField('Quantity',validators=[DataRequired()])
    usercomment = StringField('Comments', validators=[DataRequired()])                                          
    submit = SubmitField('Remove From Inventory')

# if __name__ == '__main__':
#     app.run(debug=True)