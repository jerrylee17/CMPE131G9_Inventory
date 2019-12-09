from app import app
from app import db
from flask import render_template,request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField
from app.obj.User import User
from wtforms.validators import DataRequired
from app.Pages.models import ingredientInventory,dishIngredientReq,disposalRecord
import os
from flask_login import login_required

app.config['SECRET_KEY'] = 'some-key'

def getChoices():
    """ 
    Get updated list of dishes
    
    Returns: 
        List of tuples for a selectfield with updated ingredients
    """
    dishes = dishIngredientReq.query.all()
    all = []
    for dish in dishes:
        all.append(dish.dishName)
    all = sorted(list(set(all))) #remove duplicates and sort
    df = [] #dishform
    for dish in all:
        df.append([dish.replace(" ", "_"), dish])
    return df

@app.route('/order',methods = ["GET","POST"])
@login_required
def foodOrder():
    """
    Food order page
    """
    order = dishForm()
    order.dsel.choices = getChoices()
    if order.validate_on_submit():
        dish = order.dsel.data.replace("_", " ")
        all = dishIngredientReq.query.all()
        # load up ingredient and value
        ingval = []
        for x in all:
            if x.dishName == dish:
                ingval.append([x.ingredientName2,x.quantity2])

        inv = ingredientInventory.query.all()
        idval = {}
        for i in range(len(ingval)):
            for vi in inv:
                if ingval[i][0] == vi.ingredientName:
                    if vi.quantity-ingval[i][1] > 0:
                        idval[vi.id] = vi.quantity - ingval[i][1]
                        # vi.quantity -= val[i]
                    else:
                        return redirect('/ordererr')
        for x in idval:
            dataval = ingredientInventory.query.get(x)
            dataval.quantity = idval[x]
        db.session.commit()

        

        # return render_template('order.html', order=order, signal=True)
        return redirect('/orderdone')
        
    return render_template('order.html', order=order)

@app.route('/ordererr', methods=["GET", "POST"])
@login_required
def ordErr():
    """
    Error with Food Order page
    """
    back = goBack()
    if back.validate_on_submit():
        return redirect('/order')
    return render_template('ordererr.html', back=back)

@app.route('/orderdone', methods=["GET", "POST"])
@login_required
def doneOrder():
    """
    Finished with order page
    """
    order = orderDone()
    if order.validate_on_submit():
        return redirect('/order')
    return render_template("orderDone.html", order=order)

class goBack(FlaskForm):
    """
    Form for going to the previous page
    """
    back = SubmitField('Go Back')

class dishForm(FlaskForm):
    """
    Ordering dish form
    """
    dishes = dishIngredientReq.query.all()
    all = []
    for dish in dishes:
        all.append(dish.dishName)
    all = sorted(list(set(all))) #remove duplicates and sort
    df = [] #dishform
    for dish in all:
        df.append([dish.replace(" ", "_"), dish])
    dsel = SelectField(u'Dishes ', choices=df, validators=[DataRequired()])
    order = SubmitField('Order')

class orderDone(FlaskForm):
    """
    Finished order form
    """
    ret = SubmitField('Order again')

# if __name__ == '__main__':
#     app.run()
