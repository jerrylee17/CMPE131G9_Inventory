from app import app
from app import db
from flask import render_template, request, redirect
from flask_wtf import FlaskForm
from app.Pages.models import ingredientInventory
from wtforms import StringField, IntegerField, SubmitField, FloatField, SelectField
from wtforms.validators import DataRequired
from flask_login import login_required

    
app.config['SECRET_KEY'] = 'some-key'
    
@app.route('/delivered', methods=["GET", "POST"])
@login_required
def delivered():
    form = IngredientForm()
    if form.validate_on_submit():
        amount = form.quantity.data
        if amount <= 0:
            return redirect('/deliverederr')
        selected = form.isel.data.replace("_", " ")
        inventory = ingredientInventory.query.all()
        idNumber = 0
        for i in inventory:
            if i.ingredientName == selected:
                idNumber = i.id
                break
        selectedIngredient = ingredientInventory.query.get(idNumber)
        newQuantity = selectedIngredient.quantity + amount
        selectedIngredient.quantity = newQuantity
        db.session.commit()
        return redirect('/dd')
    
    return render_template('delivered.html', form=form)

    

@app.route('/deliverederr', methods=["GET", "POST"])
@login_required
def delErr():
    back = goBack()
    if back.validate_on_submit():
        return redirect('/delivered')
    return render_template('delerr.html', back=back)

@app.route('/dd', methods=["GET", "POST"])
@login_required
def deliveredDone():
    back = goBack()
    if back.validate_on_submit():
        return redirect('/delivered')
    return render_template('dd.html', back=back)

class goBack(FlaskForm):
    back = SubmitField('Go Back')

class IngredientForm(FlaskForm):
    ingredients = ingredientInventory.query.all()
    all = []
    for ingredient in ingredients:
        all.append(ingredient.ingredientName)
    # list of all ingredients
    all = sorted(list(set(all)))
    iform = []
    for ing in all:
        iform.append([ing.replace(" ", "_"), ing])
    # iform.append(["other", "other"])
    isel = SelectField(u'Ingredient', choices=iform, validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    finished = SubmitField('Deliver ingredients')

if __name__ == '__main__':
    app.run(debug=True)
