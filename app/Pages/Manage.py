from app import app
from flask import render_template



@app.route('/manage')
def manage():
    return render_template('manage.html')


if __name__ == '__main__':
    app.run(debug=True)