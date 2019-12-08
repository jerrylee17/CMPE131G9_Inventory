import pytest
from app.Pages.models import User

@pytest.fixture(scope='module')
def new_user():
    user = User(username='sample_user_123')
    return user

def test_users(new_user):
    assert new_user.username == 'sample_user_123'