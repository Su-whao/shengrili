from flask import request, jsonify
import datetime
from db import db
from models import Birthday, User
from lib.birthday import birthCalculation

import json

def getBirthdays():
    openid = request.args.get('openid')
    user = User.query.filter(User.openid == openid).first()
    if user:
        birthdays = user.birthday_records.all()
        birthdays = [
            {
                'remarkName': b.remark_name, 
                'date': {'year': b.date.year, 'monty': b.date.month, 'day': b.date.day}
                'remark': b.remark, 
                'distance': birthCalculation.calculationBirthdayDistance(b.date),
                'relation': b.relation,
                'createTime': b.create_time.strftime('%Y-%m-%d'), 
            } 
            for b in birthdays
        ]
        return jsonify( birthdays)
    else:
        return jsonify({'msg': 'fail', 'data': 'Not the user'})

def addBirthday():
    openid = request.args.get('openid')
    remarkName = request.form.get('remarkName', None)
    remark = request.form.get('remark', None)
    date = request.form.get('date')
    relation = int(request.form.get('relation', 0))


    if not date:
        return jsonify({'msg': 'fail', 'data': 'Not input date'})
    try:
        date = json.loads(date)
        date = datetime.date(date['year'], date['month'], date['day'])
    except:
        return jsonify({'msg': 'fail', 'data': 'date parm error'})
    try:
        birthday = Birthday(
            recorder_openid=openid, 
            remark_name=remarkName, 
            remark=remrak, 
            date=date,
            remark=remark,
            relation=relation
        )
        db.session.add(birthday)
        db.session.commit()
    except Exception as e:
        print(e)
        return jsonify({'msg': 'fail', 'data': 'datebase error when add'})
    return jsonify({'msg': 'success', 'data': 'add success'})
