from app import app
from flask import render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from app.obj.User import User
from wtforms.validators import DataRequired
import os
from flask_login import login_required

app.config['SECRET_KEY'] = 'some-key'

@app.route('/order')
@login_required
def foodOrder():
    
    imagesNames = os.listdir("./app/static/images")
    return render_template('order.html', imagesNames = imagesNames)

if __name__ == '__main__':
    app.run()