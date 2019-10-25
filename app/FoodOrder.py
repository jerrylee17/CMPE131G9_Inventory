from app import app
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from app.obj.User import User
from wtforms.validators import DataRequired

app.config['SECRET_KEY'] = 'some-key'

@app.route('/order')

def foodOrder():

    return render_template('OrderPage.html')

if __name__ == '__main__':
    app.run()