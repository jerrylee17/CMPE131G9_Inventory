from app import app
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from app.obj.User import User
from flask import flash, redirect , request
from app.Pages.models import ingredientInventory,dish,disposalRecord
from app import db

app.config['SECRET_KEY'] = 'some-key'

'''db.create_all()'''
'''
userDataFile = open("app/obj/baseInventoryData.txt","r+")

for line in userDataFile:

    fields = line.split(";")

    field0 = fields[0]

    field1 = fields[1]

    field2 = fields[2]

    print (field0,field1,field2)

    temp = ingredientInventory(ingredientName=field0,quantity=field1,unitMeasure=field2)

    db.session.add(temp)
    db.session.commit()

userDataFile.close()'''
'''
userDataFile = open("app/obj/baseDishData.txt","r+")

for line in userDataFile:

    fields = line.split(";")

    field0 = fields[0]

    field1 = fields[1]

    field2 = fields[2]

    field3 = fields[3]

    print (field0,field1,field2,field3)

    temp = dish(dishName=field0,ingredientName2=field1,quantity2=field2,unitMeasure2=field3)

    db.session.add(temp)
    db.session.commit()

userDataFile.close()'''

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
