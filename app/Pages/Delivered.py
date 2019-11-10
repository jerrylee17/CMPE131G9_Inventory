from app import app
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from flask_login import login_required

# uncomment line below once you have created the
# TopCities class inside the form.py file
    
app.config['SECRET_KEY'] = 'some-key'
    
@app.route('/delivered')
@login_required
def delivered():
    
    name = 'Eric'
    
    form = Ingredients()
    
    return render_template('delivered.html', name=name, form=form)
    
    
class Ingredients(FlaskForm):
    food = SelectField(u'Ingredients', choices=[('noodles', 'Noodles'), ('pasta_sauce', 'Pasta Sauce'),
                                                ('meatballs', 'Meatballs'), ('lettuce', 'Lettuce'), ('dressing', 'Dressing')])
    quantity = IntegerField('Quantity')
    submit = SubmitField('Input')
    

if __name__ == '__main__':
    app.run()
