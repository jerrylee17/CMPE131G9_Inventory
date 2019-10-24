from flask import Flask
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
    
# uncomment line below once you have created the
# TopCities class inside the form.py file
    
app = Flask(__name__)
app.config['SECRET_KEY'] = 'some-key'
    
@app.route('/')
def home():
    
    name = 'Eric'
    
    form = TopCities()
    
    return render_template('DeliveredPage.html', name=name, form=form)
    
    
class TopCities(FlaskForm):
    food = SelectField(u'Ingredients', choices=[('noodles', 'Noodles'), ('pasta_sauce', 'Pasta Sauce'),
                                                ('meatballs', 'Meatballs'), ('lettuce', 'Lettuce'), ('dressing', 'Dressing')])
    quantity = IntegerField('Quantity')
    submit = SubmitField('Input')
    

if __name__ == '__main__':
    app.run()
