from app import app
from app import db
from flask import render_template, request, redirect
from flask_wtf import FlaskForm
from app.Pages.models import dishIngredientReq
from wtforms import StringField, IntegerField, SubmitField, FloatField, SelectField
from wtforms.validators import DataRequired
from flask_login import login_required

app.config['SECRET_KEY'] = 'some-key'

@app.route('/makemenu', methods = ["GET","POST"])
@login_required
def makemenu():
    """
    Make a new dish page
    """
    form = ing()
    done = butn()
    
    selections = ("unit", "gr", "ml")
    if done.validate_on_submit():
        if done.name.data:
            dish = done.name.data
        else:
            return redirect('/errorDish/' + "formErr" )
        i = 0
        while True:
            ig, q, m = "ingredient"+str(i),"quantity"+str(i), "measure"+str(i)
            try:
                ingredient = request.form[ig]
                quantity = request.form[q]
                measure = request.form.get(m)
                print(measure)
                if not ingredient or not quantity or not measure:
                    return redirect('/errorDish/' + "dishVoid")
                if measure not in selections:
                    return redirect('errorDish/' + "measure")
                try:
                    quantity = int(quantity)
                except:
                    return redirect('errorDish/' + "notint")
                if quantity <= 0:
                    return redirect('errorDish/' + "lt0")
                # print(request.form[ig])
                print(ingredient)
                d = dishIngredientReq(dishName=dish, ingredientName2=ingredient, quantity2=quantity, unitMeasure2=measure)
                print(d)
                db.session.add(d)
                i += 1
            except:
                break
        db.session.commit()
        return redirect('/dishMade')

    return render_template('makemenu.html', form=form, done=done)

@app.route('/dishMade', methods = ["GET", "POST"])
def madeDish():
    """
    Dish successfully made page
    """
    back = err()
    if back.validate_on_submit():
        return redirect('/makemenu')
    return render_template('menuDone.html', back=back)

@app.route('/errorDish/<string:errtype>', methods = ["GET", "POST"])
def errordish(errtype):
    """
    Dish has an error page

    Args:
        errtype(string): Type of error determined by system
    """
    back = err()
    if back.validate_on_submit():
        return redirect('/makemenu')
    return render_template('errDish.html', signal=errtype, back=back)

class butn(FlaskForm):
    """
    Wrapper form of the dynamic webpage that has the dish name and create button
    """
    name = StringField('Dish Name', validators=[DataRequired()])
    clicky = SubmitField('Create Dish')

class ing(FlaskForm):
    """
    +++NOT USED+++

    Initially was the dynamic part of the webpage that would stack when a button was pressed
    """
    ingredient = StringField('Ingredient: ', validators=[DataRequired()])
    quantity = FloatField('Quantity: ',validators=[DataRequired()])
    measures = [('unit', 'unit'), ('gr','gr'), ('ml', 'ml')]
    measure = SelectField(u'Measure: ', choices=measures, validators=[DataRequired()])
    
    # ingredient = StringField('Ingredient: ')
    # quantity = FloatField('Quantity: ')
    # measures = [('unit', 'unit'), ('gr','gr'), ('ml', 'ml')]
    # measure = SelectField(u'Measure: ', choices=measures)

class err(FlaskForm):
    """
    Error form for default error page
    """
    back = SubmitField('Go back')

# if __name__ == '__main__':
#     app.run(debug=True)
