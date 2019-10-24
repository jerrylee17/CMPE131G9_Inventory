from flask import Flask
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from User import User

userList = []

userDataFile = open("userData.txt","r+")

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


# uncomment line below once you have created the
# TopCities class inside the form.py file

app = Flask(__name__)
app.config['SECRET_KEY'] = 'some-key'

@app.route('/')
def home():

    name = 'Eric'

    form = TopCities()

    return render_template('loginPage.html', name=name, form=form)


class TopCities(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Sign In')
    

if __name__ == '__main__':
    app.run()
