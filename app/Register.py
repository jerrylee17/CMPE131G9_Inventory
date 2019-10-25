from app import app
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from app.obj.User import User
from wtforms.validators import DataRequired

app.config['SECRET_KEY'] = 'some-key'

@app.route('/registration')

def register():

    form = registration()

    return render_template('registerpage.html',form = form)


class registration(FlaskForm):

    username = StringField("Username",validators=[DataRequired()])

    password = PasswordField("Password",validators=[DataRequired()])

    passwordVer = PasswordField("Password_Verification",validators=[DataRequired()])

    submit = SubmitField("Sign In")

if __name__ == '__main__':
    app.run()