from app import app
from flask import render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from app.obj.User import User
from wtforms.validators import DataRequired
import os

app.config['SECRET_KEY'] = 'some-key'

@app.route('/order')

def foodOrder():
    
    imagesNames = os.listdir("./app/templates/static/images")
    return render_template('OrderPage.html',imagesNames = imagesNames)

if __name__ == '__main__':
    app.run()