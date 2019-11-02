from app import app
from flask import render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField
from app.obj.User import User
from wtforms.validators import DataRequired
import os

app.config['SECRET_KEY'] = 'some-key'

@app.route('/stock',methods = ["GET","POST"])

def stock():

    print("entered stock")

    form = checkForm()

    if form.validate_on_submit():

        print("entered validate")
        if form.submit1.data:
            return "mike1"
        elif form.submit2.data:
            return"da3"

    return render_template('stock.html',form=form)

@app.route('/checkIngredientByDish',methods = ["GET","POST"])

def byDish(FlaskForm):

    dishForm = usingDish()

    return render_template('checkIngredientByDish.html',dishForm=dishForm)

class checkForm(FlaskForm):

    submit1 = SubmitField("By Dish")
    submit2 = SubmitField("By Ingredient")

class usingDish(FlaskForm):

    dish = SelectField(u'Ingredients', choices=["Pasta Alfredo","Vietnamese Soup","Chicken Teriyaki"])
    submit3 = SubmitField('Confirm')

if __name__ == '__main__':
    app.run(debug=True)