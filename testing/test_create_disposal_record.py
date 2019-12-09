import pytest
from app.Pages.models import disposalRecord

@pytest.fixture(scope='module')
def new_disposal_record():
    disposal = disposalRecord(userName = "bob420", ingredientName3='rasberries', quantity3=200, unitMeasure3='gr', comment = 'I hate rasberries')
    return disposal

def test_create_disposal_record(new_disposal_record):
    assert new_disposal_record.userName == 'bob420'
    assert new_disposal_record.ingredientName3 == 'rasberries'
    assert new_disposal_record.quantity3 == 200
    assert new_disposal_record.comment == 'I hate rasberries'