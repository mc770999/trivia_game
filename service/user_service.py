from toolz import pipe,reduce
from toolz.curried import partial

from model.user_model import User

def convert_to_user(u):
    k = u
    print(k)
    a = u["name"]["first"]
    b = u["name"]["last"]
    c = u["email"]
    return  User(u['name']['first'],u['name']['last'],u['email'])

