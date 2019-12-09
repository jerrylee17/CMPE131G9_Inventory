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

@app.route('/manage')
@login_required
def manage():

    disp = disposalRecord.query.all()

    list = []

    for i in disp:

        record = " "+str(i.id)+". "+i.ingredientName3+" "+str(i.quantity3)+i.unitMeasure3+"  Comment:"+i.comment

        list.append(record)
        
    return render_template('manage.html',list=list)

# if __name__ == '__main__':
#     app.run(debug=True)