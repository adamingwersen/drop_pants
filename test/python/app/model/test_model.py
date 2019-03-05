from urllib3.util.url import Url
from app.model.model import User


def test_user_home_url():
    u = User()
    assert(isinstance(u.get_home_url(), Url))


def test_user_id():
    u = User()
    assert(u.id == '000')


def test_superuser_span():
    u = User()
    homepage = u.span_homepage_html_title()
    assert('span' in homepage)


def test_superuser_password():
    u = User()
    u.set_password('puha')
    assert(u.password == 'puha')
