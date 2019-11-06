from app import db


class ingredientInventory(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    ingredientName = db.Column(db.String(64),index = True,unique=True)
    quantity = db.Column(db.Float)
    unitMeasure = db.Column(db.String(4))
    def __repr__(self):
        return f'<ingredientInventory:{self.ingredientName},{self.quantity},{self.unitMeasure}>'

class dish(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    dishName = db.Column(db.String(64),index = True)
    ingredientName2 = db.Column(db.String(64),index = True)
    quantity2 = db.Column(db.Float)
    unitMeasure2 = db.Column(db.String(4))

    def __repr__(self):
        return f'<dish:{self.dishName},{self.ingredientName2},{self.quantity2},{self.unitMeasure2}>'

class disposalRecord(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(64),index = True)
    ingredientName3 = db.Column(db.String(64),index = True)
    quantity3 = db.Column(db.Float)
    unitMeasure3 = db.Column(db.String(4))
    comment = db.Column(db.String(256))

    def __repr__(self):
        return f'<dish:{self.userName},{self.ingredientName3},{self.quantity3},{self.unitMeasure3},{self.comment}>'
