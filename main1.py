from flask import Flask
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField

# uncomment line below once you have created the
# TopCities class inside the form.py file

app = Flask(__name__)
app.config['SECRET_KEY'] = 'some-key'

@app.route('/')
def home():

    name = 'Eric'

    form = TopCities()

    return render_template('home1.html', name=name, form=form)


class TopCities(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Sign In')
    

if __name__ == '__main__':
    app.run()
