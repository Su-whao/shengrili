
from db import db
from datetime import datetime
import shortuuid

# 用户
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.String(30), primary_key=True, default=lambda: 'u_'+shortuuid.uuid())
    openid = db.Column(db.String(50), nullable=False, unique=True, index=True)
    gender = db.Column(db.Integer, default=0)
    status = db.Column(db.Integer, default=0)
    remindWay = db.Column(db.String(20), default='[false, false]')
    phoneNum = db.Column(db.String(15), default='')
    email = db.Column(db.String(30), default='')
    region = db.Column(db.String(50), default='{"country":"", "province":"", "city":""}')

    create_time = db.Column(db.DateTime, default=datetime.now)
    modify_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

# birthday record
class Birthday(db.Model):
    __tablename__ = 'birthday'
    id = db.Column(db.String(30), primary_key=True, default=lambda: 'b_'+shortuuid.uuid())
    recorder_openid = db.Column(db.String(30), db.ForeignKey('user.openid'), nullable=False)
    recorder = db.relationship('User', backref=db.backref('birthday_records', lazy='dynamic'))
    remark_name = db.Column(db.String(20))
    remark = db.Column(db.String(50))
    date = db.Column(db.Date, nullable=False)
    relationship = db.Column(db.Integer,default=0)

    create_time = db.Column(db.DateTime, default=datetime.now)
    modify_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)