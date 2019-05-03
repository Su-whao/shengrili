from flask import Blueprint, request
from apps.birthday import view

birthday = Blueprint('birthday', __name__)

@birthday.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'GET':
        return view.getBirthdays()
    else:
        return view.addBirthday()