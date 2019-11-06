from app import app
from flask import render_template,request
from flask_wtf import FlaskForm
from app.obj.User import User
from app.obj.Dish import Dish
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, IntegerField


app.config['SECRET_KEY'] = 'some-key'

@app.route('/makemenu', methods = ["GET","POST"])

def makemenu():
    dish = Dish()
    ingredient = StringField('Ingredient')
    quantity = IntegerField('Quantity')
    return render_template('makemenu.html')

class menu(FlaskForm):
    pass


if __name__ == '__main__':
    app.run()