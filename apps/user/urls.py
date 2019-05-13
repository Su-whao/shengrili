from flask import Blueprint, request
from apps.user import view

user = Blueprint('user', __name__)


@user.route('/', methods=['POST'])
def root():
    return view.addUser()

@user.route('/<openid>', methods=['GET', 'POST'])
def  userinfo(openid):
    if request.method == 'GET':
        return view.getUser(openid)
    else:
        return view.update(openud)
