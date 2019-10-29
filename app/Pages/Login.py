from app import app
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from app.obj.User import User
from flask import flash, redirect , request

"""
userList = []

userDataFile = open("app/obj/userData.txt","r+")

counter = 0

for line in userDataFile:

    fields = line.split(";")
    field1 = fields[0]
    #print (field1)
    field2 = fields[1]
    #print (field2)
    field3 = fields[2]
    #print (field3)

    temp = User(field1,field2,field3)

    userList.append(temp)

userDataFile.close()

for User in userList:

    print (User.username)


app.config['SECRET_KEY'] = 'some-key'
"""
@app.route('/login',methods = ["GET","POST"])
def login():

    form = TopCities()

    if form.validate_on_submit():
        flash("Succesfull Login")
        return redirect("/dispose")

    return render_template('login.html', form=form)

sampleUsername = "person123"

def validate_proof(form, field):
        if field.data != sampleUsername:
            raise ValidationError('Wrong password.')

class TopCities(FlaskForm):

    sampleUsername = "person123"
    samplePassword = "p"

    username = StringField("Username", [DataRequired(), validate_proof])
    password = PasswordField("Password", validators=[DataRequired()])#,EqualTo("samplePassword", "Invalid password")])
    submit = SubmitField("Sign In")

    

if __name__ == "__main__":
    app.run()
