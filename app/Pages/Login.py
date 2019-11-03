from app import app
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from app.obj.User import User
from flask import flash, redirect , request

app.config['SECRET_KEY'] = 'some-key'

@app.route('/login',methods = ["GET","POST"])
def login():

    form = TopCities()

    if form.validate_on_submit():
        flash("Succesfull Login")
        return redirect("/dispose")

    return render_template('login.html', form=form)

sampleUsername = "person123"

userPassword = ""

def validate_username(form, field):

    global userPassword

    validUser = False
    userNum = 0

    for user in userList:
        if field.data == user.username:
            validUser = True
            break
        userNum += 1

    if validUser == False:
        print('Wrong username')
        raise ValidationError('Wrong username')
    else:
        print(userList[userNum].password)
        userPassword = userList[userNum].password
        print(userPassword)


def validate_password(form, field):
    print(userPassword)
    print(field.data)
    if field.data != userPassword:
        raise ValidationError('Wrong username or password.')

class TopCities(FlaskForm):

    sampleUsername = "person123"
    samplePassword = "p"

    username = StringField("Username", [DataRequired(), validate_username])
    password = PasswordField("Password", [DataRequired(), validate_password])
    submit = SubmitField("Sign In")

    

if __name__ == "__main__":
    app.run()
