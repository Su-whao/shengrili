from flask import request, jsonify
from models import User, Birthday
from db import db
from lib.modelFunc import modelFunc
import requests
import json

def getUser(openid):
    user = User.query.filter(User.openid == openid).first()
    user = modelFunc.model_to_dict(user)
    if user:
        try:
            user['birthday'] = {'year': user['birthday'].year, 'month': user['birthday'].month, 'day': user['birthday'].day} \
                    if user['birthday'] \
                    else {'year': '', 'month': '', 'day': ''}
            user['remindWay'] = json.loads(user['remindWay'])
            user['region'] = json.loads(user['region'])
            user['registerData'] = {'year': user['create_time'].year, 'month': user['create_time'].month, 'day': user['create_time'].day}
            del user['modify_time']
            del user['create_time']
        except Exception as e:
            print(e)
            return jsonify({'msg': 'fail', 'data': 'db commit error'})
        return jsonify(user)
    else:
        return jsonify({'msg': 'fail', 'data': 'Not the user'})

def addUser():
    openid = request.form.get('openid')
    if not openid:
        return jsonify({'msg': 'fail', 'data': 'openid is empty'})
    try:
        user = User(openid=openid)
        db.session.add(user)
        db.session.commit()
    except:
        return jsonify({'msg': 'fail', 'data': 'db commit error'})
    return openid

def update(openid):
    field = request.form.get('field')
    data = request.form.get('data')
    if not openid:
        return jsonify({'msg': 'fail', 'data': 'openid is empty'})
    if not field:
        return jsonify({'msg': 'fail', 'data': 'field is empty'})

    user = User.query.filter(User.openid == openid)
    try:
        user.update({field: data})
        db.session.commit()
    except Exception as e:
        print(e)
        return jsonify({'msg': 'fail', 'data': 'db commit error'})
    return jsonify({'msg': 'success', 'data': 'update {} to {} success'.format(field, data)})

def wxLogin():
    code = request.form.get('code')
    if not code:
        return jsonify({'msg': 'fail', 'data': 'code is null'})
    APPID = ''
    SECRET = ''
    wxLoginResult = requests.get('https://api.weixin.qq.com/sns/jscode2session?appid={}&secret={}}&js_code={}}&grant_type=authorization_code'.format(APPID, SECRET, code))
    return jsonify(wxLoginResult.json)

