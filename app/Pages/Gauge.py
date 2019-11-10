from app import app
from flask import render_template
from flask_login import login_required

@app.route('/gauge')
@login_required
def gauge():
    return render_template('gauge.html')


if __name__ == '__main__':
    app.run(debug=True)