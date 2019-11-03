from app import app
from flask import render_template,request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField
from app.obj.User import User
from wtforms.validators import DataRequired
import os

app.config['SECRET_KEY'] = 'some-key'

@app.route('/dispose',methods=["GET","POST"])
def dispose():

    form = disposal()
    return render_template('dispose.html',form=form)

class disposal(FlaskForm):

    ingredient = SelectField(u'Ingredient', choices=[('noodles', 'Noodles'), ('pasta_sauce', 'Pasta Sauce'),
                                                ('meatballs', 'Meatballs'), ('lettuce', 'Lettuce'), ('dressing', 'Dressing')])
    
    measure = SelectField(u'Measure', choices=[('unit', 'unit'),('mililiter', 'ml'), ('gram', 'gr')])

    quantity = IntegerField('Quantity',validators=[DataRequired()])

    usercomment = StringField('Comments', validators=[DataRequired()])                                          
    
    submit = SubmitField('Remove From Inventory')

if __name__ == '__main__':
    app.run(debug=True)