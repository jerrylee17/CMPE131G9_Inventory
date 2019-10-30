class Ingredient():

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __repr__(self):
        s = str(self.name)+" has " + str(self.quantity) + " left."
        return s