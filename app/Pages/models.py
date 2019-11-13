from datetime import datetime
from app import db
from app import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)    

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class ingredientInventory(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    ingredientName = db.Column(db.String(64),index = True,unique=True)
    quantity = db.Column(db.Float)
    unitMeasure = db.Column(db.String(4))
    def __repr__(self):
        return f'<ingredientInventory:{self.ingredientName},{self.quantity},{self.unitMeasure}>'

class dishIngredientReq(db.Model):
    # __tablename__ = "dish"
    id = db.Column(db.Integer, primary_key=True)
    dishName = db.Column(db.String(64),index = True)
    ingredients = db.relationship('dishIngre', backref='dish', lazy='dynamic')
    # ingredientName2 = db.Column(db.String(64),index = True)
    # quantity2 = db.Column(db.Float)
    # unitMeasure2 = db.Column(db.String(4))

    def __repr__(self):
        return f'<dishIngredientReq:{self.dishName},{self.ingredientName2},{self.quantity2},{self.unitMeasure2}>'

class dishIngre(db.Model):
    # __tablename__ = "dishing"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64),index = True,unique=True)
    quantity = db.Column(db.Float)
    unit = db.Column(db.String(4))
    dish_id = db.Column(db.Integer, db.ForeignKey('dish_ingredient_req.id'), nullable=False)

    def __repr__(self):
        return f'<ingredientInventory:{self.ingredientName},{self.quantity},{self.unitMeasure}>'

class disposalRecord(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(64),index = True)
    ingredientName3 = db.Column(db.String(64),index = True)
    quantity3 = db.Column(db.Float)
    unitMeasure3 = db.Column(db.String(4))
    comment = db.Column(db.String(256))

    def __repr__(self):
        return f'<dishIngredientReq:{self.userName},{self.ingredientName3},{self.quantity3},{self.unitMeasure3},{self.comment}>'
