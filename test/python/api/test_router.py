from urllib3.util.url import Url
from api.router import get_url


def test_get_url():
    assert(isinstance(get_url('http://raffle.ai'), Url))
