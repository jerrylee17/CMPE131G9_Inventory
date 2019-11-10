from app import app
from flask import render_template
from flask_login import login_required

@app.route('/manage')
@login_required
def manage():
    return render_template('manage.html')


if __name__ == '__main__':
    app.run(debug=True)