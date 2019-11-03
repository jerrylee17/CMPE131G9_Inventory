from app import app
from flask import render_template,request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField
from app.obj.User import User
from wtforms.validators import DataRequired
import os

app.config['SECRET_KEY'] = 'some-key'

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

    dish = SelectField(u'Dishes', choices=[("Pasta_Alfredo","Pasta Alfredo"),("Vietnamese_Soup","Vietnamese Soup"),("Chicken_Teriyaki","Chicken Teriyaki")])

    submit3 = SubmitField('GO')

class usingIngredient(FlaskForm):

    ingredient = SelectField(u'Ingredients', choices=[('noodles', 'Noodles'), ('pasta_sauce', 'Pasta Sauce'),
                                                ('meatballs', 'Meatballs'), ('lettuce', 'Lettuce'), ('dressing', 'Dressing')])

    submit4 = SubmitField('GO')

if __name__ == '__main__':
    app.run(debug=True)