from flask import Blueprint, request
from apps.birthday import view

birthday = Blueprint('birthday', __name__)

@birthday.route('/<openid>', methods=['GET', 'POST'])
def root(openid):
    if request.method == 'GET':
	    return view.getBirthdays(openid)
    else:		
        return view.addBirthday(openid)

@birthday.route('/<openid>/<bid>', methods=['POST'])
def update(openid, bid):
	return view.update(openid, bid)
