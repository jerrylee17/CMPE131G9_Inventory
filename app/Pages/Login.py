from app import app
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from app.obj.User import User
from app.Pages.models import User
from flask import flash, redirect , request, url_for
from app.Pages.models import ingredientInventory,dishIngredientReq,disposalRecord
from app import db
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required
from werkzeug.urls import url_parse

app.config['SECRET_KEY'] = 'some-key'

@app.route('/login',methods = ["GET","POST"])
def login():
    """
    Login page
    """
    if current_user.is_authenticated:
        return redirect('/main')

    form = Login()
    if form.validate_on_submit():
        # look at first result first()
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect('/login')
            flash('Invalid username or password')
        login_user(user)
        # return to page before user got asked to login
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')

        return redirect(next_page)
    return render_template('login.html', title='Sign in', form=form)

# sampleUsername = "person123"

# userPassword = ""

"""
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
"""

@app.route('/logout')
def logout():
    """
    Logout page
    
    Returns:
        Immediately returns to the login page
    """
    logout_user()
    return redirect('/login')


class Login(FlaskForm):
    """
    Login form
    """

    sampleUsername = "person123"
    samplePassword = "p"
    username = StringField("Username", [DataRequired()])
    password = PasswordField("Password", [DataRequired()])
    submit = SubmitField("Sign In")

    

# if __name__ == "__main__":
#     app.run()
