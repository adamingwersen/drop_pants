from api.router import get_url


class User():
    def __init__(self):
        self.id = '000'
        self.home_url = get_url('http://raffle.ai')
        self.homepage_html_title = 'A title'

    def get_home_url(self):
        return(self.home_url)

    def span_homepage_html_title(self):
        return('<span>{}</span>'.format(self.homepage_html_title))

    def set_password(self, password):
        self.password = password
