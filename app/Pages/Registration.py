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

@app.route('/register',methods = ["GET","POST"])

def register():
    """
    Registration page
    """
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = register()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect('/login')
    return render_template('register.html', title='Register', form=form)
    
class register(FlaskForm):
    """
    Registration form
    """
    #print("entered registration")
    
    username = StringField("Username",validators=[DataRequired(),Length(max=10)])
    password = PasswordField("Password",validators=[DataRequired(),Length(max=10)])
    passwordVer = PasswordField("Password Verification",validators=[DataRequired(),EqualTo("password","password does not match")])
    submit = SubmitField("Register")
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            flash('Please use a different username.')
            raise ValidationError('Please use a different username.')

# if __name__ == '__main__':
#     app.run()