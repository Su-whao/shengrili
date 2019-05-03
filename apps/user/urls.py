from flask import Blueprint, request
from apps.user import view

user = Blueprint('user', __name__)

@user.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'GET':
        return view.getUser()
    else:
        return view.addUser()