from app import app
from flask import render_template

@app.route('/dispose')
def dispose():
    return render_template('dispose.html')

if __name__ == '__main__':
    app.run(debug=True)