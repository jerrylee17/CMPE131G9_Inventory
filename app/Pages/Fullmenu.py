from app import app
from flask import render_template, redirect
from flask_login import login_required
from app.Pages.models import dishIngredientReq

@app.route('/alldishes', methods=["GET"])
@login_required
def fullmenu():
    """
    Display the full menu page
    """
    dishes = dishIngredientReq.query.all()
    all = []
    for dish in dishes:
        all.append(dish.dishName)
    all = sorted(list(set(all)))
    for i, x in enumerate(all):
        all[i] = (i,x)
    return render_template('fullmenu.html', all=all)

# if __name__ == '__main__':
#     app.run(debug=True)