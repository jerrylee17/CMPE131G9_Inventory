from app import app
from flask import render_template,request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField, FloatField
from app.obj.User import User
from wtforms.validators import DataRequired
import os
from app.Pages.models import ingredientInventory,dishIngredientReq,disposalRecord
from app import db
from flask import flash, redirect , request
from flask_login import login_required

def invertList(input_list): 
   input_list.reverse()
   return input_list

@app.route('/manage', methods=["GET", "POST"])
@login_required
def manage():
    """
    Disposal record page
    """
    disp = disposalRecord.query.all()
    clear = clr()

    idNumber, ingredient, quantity, reason = [], [], [], []
    
    for i in disp:

        number = i.id
        ingre = i.ingredientName3
        quan = str(i.quantity3)+"   "+i.unitMeasure3
        rea = i.comment

        idNumber.append(number)
        ingredient.append(ingre)
        quantity.append(quan)
        reason.append(rea)

    idNumber=invertList(idNumber)
    ingredient=invertList(ingredient)
    quantity=invertList(quantity)
    reason=invertList(reason)
    if clear.validate_on_submit():
        disposalRecord.query.delete()
        db.session.commit()
        return redirect('/manage')

    return render_template('manage.html',idNumber=idNumber,ingredient=ingredient,quantity=quantity,reason=reason, clr=clear)

   



class clr(FlaskForm):
    """
    Clear disposal record
    """
    clicky = SubmitField('Clear record')

# if __name__ == '__main__':
#     app.run(debug=True)