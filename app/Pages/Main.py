from app import app
from flask import render_template,request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField
from app.obj.User import User
from wtforms.validators import DataRequired
import os
from app.Pages.models import ingredientInventory,dishIngredientReq,disposalRecord
from app import db
from flask_login import login_required


@app.route('/')
def index():
    """
    Main page when not logged in
    """
    return redirect('/login')

@app.route('/main',methods = ["GET","POST"])
def main():
    form = checkForm()

    if form.validate_on_submit():
        if form.currentMenu.data:
            return redirect("/alldishes")
        elif form.newDish.data:
            return redirect("/makemenu")
        elif form.stock.data:
            return redirect("/stock")
        elif form.dispose.data:
            return redirect("/dispose")

    return render_template('main.html',form = form)

class checkForm(FlaskForm):

    currentMenu = SubmitField("Current Menu")
    newDish = SubmitField("New Dish")
    stock = SubmitField("Stock")
    dispose = SubmitField("Dispose")

# if __name__ == '__main__':
#     app.run(debug=True)