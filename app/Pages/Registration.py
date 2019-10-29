from app import app
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from app.obj.User import User
from wtforms.validators import DataRequired, Length, EqualTo
from flask import flash, redirect , request

app.config['SECRET_KEY'] = 'some-key'

@app.route('/registration',methods = ["GET","POST"])

def register():

    form = registration()

    #if form.validate_on_submit():

    #  print("entered if")
        
    #  return redirect(url_for('login'))

    if form.validate_on_submit():
        flash("Succesfull Registration")
        return redirect("/login")
   
    return render_template('registration.html',form = form)
    
class registration(FlaskForm):

    #print("entered registration")
    
    username = StringField("Username",validators=[DataRequired(),Length(max=10)])

    password = PasswordField("Password",validators=[DataRequired(),Length(max=10)])

    passwordVer = PasswordField("Password Verification",validators=[DataRequired(),EqualTo("password","password does not match")])

    submit = SubmitField("Register")

if __name__ == '__main__':
    app.run()