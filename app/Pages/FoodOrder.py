from app import app
from app import db
from flask import render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField
from app.obj.User import User
from wtforms.validators import DataRequired
from app.Pages.models import ingredientInventory,dishIngredientReq,disposalRecord
import os
from flask_login import login_required

app.config['SECRET_KEY'] = 'some-key'

@app.route('/order',methods = ["GET","POST"])
@login_required
def foodOrder():
    order = dishForm()
    if order.validate_on_submit():
        dish = order.dsel.data.replace("_", " ")
        all = dishIngredientReq.query.all()
        ing, val = [], []
        for x in all:
            if x.dishName == dish:
                ing.append(x.ingredientName2)
                val.append(x.quantity2)

        inv = ingredientInventory.query.all()
        flag = False
        for i in range(len(ing)):
            for vi in inv:
                if ing[i] == vi.ingredientName:
                    if vi.quantity-val[i] > 0:
                        vi.quantity -= val[i]
                    else:
                        flag = True
                        break
            if flag:
                break

        if not flag:
            db.session.commit()
        

        return render_template('order.html', order=order, signal=True)
        
    return render_template('order.html', order=order)

class dishForm(FlaskForm):
    dishes = dishIngredientReq.query.all()
    all = []
    for dish in dishes:
        all.append(dish.dishName)
    all = sorted(list(set(all))) #remove duplicates and sort
    df = [] #dishform
    for dish in all:
        df.append([dish.replace(" ", "_"), dish])
    dsel = SelectField(u'Dishes', choices=df, validators=[DataRequired()])
    order = SubmitField('Order')


if __name__ == '__main__':
    app.run()
