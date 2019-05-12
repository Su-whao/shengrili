from flask import request, jsonify
from models import User, Birthday
from db import db
import requests

def getUser():
    openid = request.args.get('openid')
    user = User.query.filter(User.openid == openid).first()
    if user:
        return jsonify({'msg': 'success', 'data': user.birthday})
    else:
        return jsonify({'msg': 'fail', 'data': 'Not the user'})    

def addUser():
    openid = request.form.get('openid')
    try:
        user = User(openid=openid)
        db.session.add(user)
        db.session.commit()
    except:
        return jsonify({'msg': 'fail', 'data': 'database error when add'})
    return jsonify({'msg': 'success', 'data': 'add success'})

def wxLogin():
    code = request.form.get('code')
    if not code:
        return jsonify({'msg': 'fail', 'data': 'code is null'})
    APPID = ''
    SECRET = ''
    wxLoginResult = requests.get('https://api.weixin.qq.com/sns/jscode2session?appid={}&secret={}}&js_code={}}&grant_type=authorization_code'.format(APPID, SECRET, code))
    return jsonify({'msg': 'success', 'data': wxLoginResult})

