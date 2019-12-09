import pytest
from app.Pages.models import dishIngredientReq

@pytest.fixture(scope='module')
def new_dish():
    dish = dishIngredientReq(dishName='macaroni 123', ingredientName2='cheese', quantity2=150, unitMeasure2='gr')
    return dish

def test_create_dish(new_dish):
    assert new_dish.dishName == 'macaroni 123'
    assert new_dish.ingredientName2 == 'cheese'
    assert new_dish.quantity2 == 150
    assert new_dish.unitMeasure2 == 'gr'
    