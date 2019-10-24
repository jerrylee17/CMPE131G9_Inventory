from flask import Flask

app = Flask(__name__)


@app.route('/')

def home():
    return render_template('MainPage.html', name=name, form=form)


if __name__ == '__main__':
    app.run()