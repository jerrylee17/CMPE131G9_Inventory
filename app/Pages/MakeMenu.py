from app import app
from flask import render_template, request, redirect
from flask_wtf import FlaskForm
from app.Pages.models import dishIngredientReq, dishIngre
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, IntegerField, SubmitField, FloatField
from wtforms.validators import DataRequired
from flask_login import login_required

app.config['SECRET_KEY'] = 'some-key'

@app.route('/makemenu', methods = ["GET","POST"])
@login_required
def makemenu():
    form = ing()
    done = butn()

    # if done.validate_on_submit():
    #     if done.name.data:
    #         dish = dishIngredientReq(dishName=done.name.data)
    #         ing = dishIngre(name=form.name.data, quantity=form.quantity.data, measure=form.measure.data)

    return render_template('makemenu.html', form=form, done=done)

@app.route('/dishMade', methods = ["GET", "POST"])
def madeDish():
    return render_template('menuDone.html')

class butn(FlaskForm):
    name = StringField('Dish Name')
    clicky = SubmitField('Create Dish')

class ing(FlaskForm):
    ingredient = StringField('Ingredient: ', validators=[DataRequired()])
    quantity = FloatField('Quantity: ',validators=[DataRequired()])
    measure = StringField('Measure: ', validators=[DataRequired()])


if __name__ == '__main__':
    app.run(debug=True)