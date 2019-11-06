from app import app
from flask import render_template,request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField, FloatField
from app.obj.User import User
from wtforms.validators import DataRequired
import os
from app.Pages.models import ingredientInventory,dish,disposalRecord
from app import db
from flask import flash, redirect , request

app.config['SECRET_KEY'] = 'some-key'

@app.route('/dispose',methods=["GET","POST"])
def dispose():

    form = disposal()

    if form.validate_on_submit():

        selected = form.ingredient.data.replace("_", " ")

        inventory = ingredientInventory.query.all()

        idNumber = 0

        for i in inventory:

            if i.ingredientName == selected:
            
                idNumber = i.id

                break

        selectedIngredient = ingredientInventory.query.get(idNumber)

        if selectedIngredient.unitMeasure[:-1] != form.measure.data:
           
            flash("Incorrect Unit Measure")
            return redirect("/dispose")

        elif form.quantity.data>selectedIngredient.quantity:

            flash("Available stock is less than que quantity to be disposed")
            return redirect("/dispose")

        
        newQuantity = selectedIngredient.quantity - form.quantity.data

        selectedIngredient.quantity = newQuantity
        db.session.commit()

        temp = disposalRecord(userName = "Logged User",ingredientName3=selected,quantity3=form.quantity.data,unitMeasure3=form.measure.data,comment=form.usercomment.data)

        db.session.add(temp)
        db.session.commit()
        
        flash("Removal successfull")
        return redirect("/dispose")
        #elif(selectedIngredient.quantity != form.measure)

    return render_template('dispose.html',form=form)

class disposal(FlaskForm):

    inventoryTemp = ingredientInventory.query.all()

    generalList=[]

    for item in inventoryTemp:
    
        object1 = item.ingredientName
        object2 = item.ingredientName

        generalList.append([object1.replace(" ", "_"),object2])

    ingredient = SelectField(u'Ingredient', choices=generalList)
    
    measure = SelectField(u'Measure', choices=[('unit', 'unit'),('ml', 'ml'), ('gr', 'gr')])

    quantity = FloatField('Quantity',validators=[DataRequired()])

    usercomment = StringField('Comments', validators=[DataRequired()])                                          
    
    submit = SubmitField('Remove From Inventory')

if __name__ == '__main__':
    app.run(debug=True)