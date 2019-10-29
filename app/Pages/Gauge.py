from app import app
from flask import render_template

@app.route('/gauge')
def gauge():
    return render_template('gauge.html')


if __name__ == '__main__':
    app.run(debug=True)