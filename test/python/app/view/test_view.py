from app.view.view import check_password
from app.model.model import User


def test_check_password():
    u = User()
    u.set_password('puha')
    assert(check_password('puha', u) is True)
