from app import app
from flask import render_template, redirect
from flask_login import login_required


@app.route('/')
def index():
    """
    Main page when not logged in
    """
    return redirect('/login')

@app.route('/main')
def main():
    """
    Main page
    """
    return render_template('main.html')


# if __name__ == '__main__':
#     app.run(debug=True)