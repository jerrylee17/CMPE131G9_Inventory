import pytest
from app.Pages.models import ingredientInventory

@pytest.fixture(scope='module')
def new_ingredient():
    ingredient = ingredientInventory(ingredientName='secret sauce', quantity=300, unitMeasure='ml')
    return ingredient

def test_create_ingredient(new_ingredient):
    assert new_ingredient.ingredientName == 'secret sauce'
    assert new_ingredient.quantity == 300
    assert new_ingredient.unitMeasure == 'ml'