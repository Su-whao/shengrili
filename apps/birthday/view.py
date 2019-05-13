from flask import request, jsonify
import datetime
from db import db
from models import Birthday, User
from lib.birthday import birthCalculation

import json

def getBirthdays(openid):
    user = User.query.filter(User.openid == openid).first()
    if user:
        birthdays = user.birthday_records
        birthdays = [
            {
                'id': b.id,
                'remarkName': b.remark_name, 
                'date': {'year': b.date.year, 'monty': b.date.month, 'day': b.date.day},
                'remark': b.remark, 
                'distance': birthCalculation.calculationBirthdayDistance(b.date),
                'relationship': b.relationship,
                'createTime': b.create_time.strftime('%Y-%m-%d'), 
            } 
            for b in birthdays
        ]
        return jsonify( birthdays)
    else:
        return jsonify({'msg': 'fail', 'data': 'Not the user'})

def addBirthday(openid):
    remarkName = request.form.get('remarkName', None)
    remark = request.form.get('remark', None)
    date = request.form.get('date')
    relationship = int(request.form.get('relationship', 0))

    if not openid:
        return jsonify({'msg': 'fail', 'data': 'Not the user'})

    if not date:
        return jsonify({'msg': 'fail', 'data': 'Not input date'})
    try:
        date = json.loads(date)
        date = datetime.date(date['year'], date['month'], date['day'])
    except:
        return jsonify({'msg': 'fail', 'data': 'date shoud be json string'})
    try:
        birthday = Birthday(
            recorder_openid=openid, 
            remark_name=remarkName, 
            remark=remark, 
            date=date,
            relationship=relationship
        )
        db.session.add(birthday)
        db.session.commit()
    except Exception as e:
        print(e)
        return jsonify({'msg': 'fail', 'data': 'datebase error when add'})
    return jsonify({'msg': 'success', 'data': 'add success'})

def update(openid, bid):

    field = request.form.get('field')
    data = request.form.get('data')
    if not openid:
        return jsonify({'msg': 'fail', 'data': 'openid is empty'})
    if not field:
        return jsonify({'msg': 'fail', 'data': 'field is empty'})

    if field == 'date':
        data = json.loads(data)
        try:
            data = datetime.date(data['year'], data['month'], data['day'])
        except Exception as e:
            print(e)
            return jsonify({'msg': 'fail', 'data': 'data format error'})
    elif field == 'remarkName':
        field = 'remark_name'

    birthdayRecords = User.query.filter(User.openid == openid).first().birthday_records
    usersBids = [b.id for b in birthdayRecords]

    if bid not in usersBids:
        return jsonify({'msg': 'fail', 'data': 'The birthday not belong to the user'})

    birthday = Birthday.query.filter(Birthday.id == bid)
    try:
        birthday.update({field: data})
        db.session.commit()
    except Exception as e:
        print(e)
        return jsonify({'msg': 'fail', 'data': 'db commit error'})
    return jsonify({'msg': 'success', 'data': 'update {} to {} success'.format(field, data)})
