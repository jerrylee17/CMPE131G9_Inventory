from app import app
from flask import render_template,request
from flask_wtf import FlaskForm
from app.Pages.models import dishIngredientReq
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, IntegerField, SubmitField, FloatField
from wtforms.validators import DataRequired


app.config['SECRET_KEY'] = 'some-key'

@app.route('/makemenu', methods = ["GET","POST"])

def makemenu():
    Addit = SubmitField('+')
    form = ing()
    done = butn()

    # if done.data:
    #     return redirect("/dishMade")

    return render_template('makemenu.html', form=form, done=done)

# @app.route('/dishMade', methods = ["GET", "POST"])
# def madeDish():
#     done = create()

class butn(FlaskForm):
    clicky = SubmitField('Create Dish')

class ing(FlaskForm):
    ingredient = StringField('Ingredient: ', validators=[DataRequired()])
    quantity = FloatField('Quantity: ',validators=[DataRequired()])
    measure = StringField('Measure: ', validators=[DataRequired()])


if __name__ == '__main__':
    app.run(debug=True)