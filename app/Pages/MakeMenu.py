from app import app
from flask import render_template, request, redirect
from flask_wtf import FlaskForm
from app.Pages.models import dishIngredientReq, dishIngre
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, IntegerField, SubmitField, FloatField, SelectField
from wtforms.validators import DataRequired
from flask_login import login_required

app.config['SECRET_KEY'] = 'some-key'

@app.route('/makemenu', methods = ["GET","POST"])
@login_required
def makemenu():
    form = ing()
    done = butn()
    

    if done.validate_on_submit():
        if done.name.data:
            dish = dishIngredientReq(dishName=done.name.data)
        else:
            return redirect('/errorDish')
        me = request.form["ingredient0"]
        print(me)
        return redirect('/dishMade')

    return render_template('makemenu.html', form=form, done=done)

@app.route('/dishMade', methods = ["GET", "POST"])
def madeDish():
    back = err()
    if back.validate_on_submit():
        return redirect('/makemenu')
    return render_template('menuDone.html', back=back)

@app.route('/errorDish', methods = ["GET", "POST"])
def errordish():
    back = err()
    if back.validate_on_submit():
        return redirect('/makemenu')
    return render_template('errDish.html', back=back)

class butn(FlaskForm):
    name = StringField('Dish Name', validators=[DataRequired()])
    clicky = SubmitField('Create Dish')

class ing(FlaskForm):
    ingredient = StringField('Ingredient: ', validators=[DataRequired()])
    quantity = FloatField('Quantity: ',validators=[DataRequired()])
    measures = [('unit', 'unit'), ('gr','gr'), ('ml', 'ml')]
    measure = SelectField(u'Measure: ', choices=measures, validators=[DataRequired()])
    
    # ingredient = StringField('Ingredient: ')
    # quantity = FloatField('Quantity: ')
    # measures = [('unit', 'unit'), ('gr','gr'), ('ml', 'ml')]
    # measure = SelectField(u'Measure: ', choices=measures)

class err(FlaskForm):
    back = SubmitField('Go back')

if __name__ == '__main__':
    app.run(debug=True)
