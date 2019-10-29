from app import app
from flask import render_template

@app.route('/stock')
def stock():
    return render_template('stock.html')


if __name__ == '__main__':
    app.run(debug=True)