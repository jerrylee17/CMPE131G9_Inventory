from app import app
from app import db
from flask import render_template, request, redirect, flash
from flask_wtf import FlaskForm
from app.Pages.models import ingredientInventory
from wtforms import StringField, IntegerField, SubmitField, FloatField, SelectField
from wtforms.validators import DataRequired
from flask_login import login_required



app.config['SECRET_KEY'] = 'some-key'

@app.route('/input', methods=["GET", "POST"])
@login_required
def input():
    """
    Input ingredients page
    """
    form = InputForm()
    if form.validate_on_submit():
        input2(form)
        '''
        amount = form.quantity.data
        if amount <= 0:
            return redirect('/inputerr')
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
        '''
    
    return render_template('input.html', form=form)

def input2(form):
    """
    Handle the input form onclick
    
    Args: 
        form(FlaskForm): form with the information
    """
    amount = form.quantity.data
    if amount <= 0:
        return redirect('/inputerr')
    selected = form.isel.data.replace("_", " ")
    inventory = ingredientInventory.query.all()
    idNumber = 0
    for i in inventory:
        if i.ingredientName == selected:
            idNumber = i.id
            break
    selectedIngredient = ingredientInventory.query.get(idNumber)
    newQuantity = selectedIngredient.quantity + amount
    flash('Successfully inputted ingredients')
    selectedIngredient.quantity = newQuantity
    db.session.commit()
    return redirect('/inputd')

@app.route('/inputerr', methods=["GET", "POST"])
@login_required
def inputErr():
    """
    Error with inputting ingredients page
    """
    back = goBack()
    if back.validate_on_submit():
        return redirect('/input')
    return render_template('inputerr.html', back=back)

@app.route('/inputd', methods=["GET", "POST"])
@login_required
def inputDone():
    """
    Successfully stored ingredients page
    """
    back = goBack()
    if back.validate_on_submit():
        return redirect('/input')
    return render_template('dd.html', back=back)

class goBack(FlaskForm):
    """
    Form for going to the pervious page
    """
    back = SubmitField('Go Back')

class InputForm(FlaskForm):
    """
    Input ingredients form
    """
    ingredients = ingredientInventory.query.all()
    all = []
    for ingredient in ingredients:
        all.append([ingredient.ingredientName, ingredient.unitMeasure])
    # list of all ingredients
    # all = sorted(list(set(all)))
    iform = []
    for ing in all:
        iform.append([ing[0].replace(" ", "_"), ing[0]+" ( "+ing[1]+ ")"])
    iform.append(["Other", "Other"])
    # dic = {}
    # # clean up units inside all
    # for elem in all:
    #     elem[1]=elem[1].replace("\n", "")
    #     # dictionary of ingredient to unit
    #     dic[elem[0]]= elem[1]
        
    isel = SelectField(u'Ingredient', choices=iform, validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    finished = SubmitField('Input ingredients')

if __name__ == '__main__':
    app.run(debug=True)
