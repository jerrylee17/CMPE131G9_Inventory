from app.obj.Ingredient import Ingredient
from datetime import datetime
from app import db

class Dish:
    
    def __init___(self):
        self.ingredients = {}
        self.category = None
    
    #ingredients = dict{Ingredient:int}, category = string
    def inputMenu(ingredients, category):
        self.ingredients=ingredients
        self.category=category
    
    #return ingredients
    def use():
        return ingredients

    #return object with the ingredient value changed
    #ingre = dict{Ingredient:int}
    def useOverride(ingre):
        if ingre not in ingredients:
            print("Ingredient not found")
            return
        resultSet = ingredients
        resultSet.update(ingre)
        return resultSet
    