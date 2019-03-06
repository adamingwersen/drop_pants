from app.view.view import check_password
from app.model.model import User


if __name__ == '__main__':
    u = User()
    u.set_password('puha')
    b = check_password('puha', u)
    print('What an app..')
