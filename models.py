
from db import db
from datetime import datetime
import shortuuid

# 用户
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.String(30), primary_key=True, default=lambda: 'u_'+shortuuid.uuid())
    openid = db.Column(db.String(50), nullable=False, unique=True, index=True)
    birthday = db.Column(db.DateTime)

    create_time = db.Column(db.DateTime, default=datetime.now)
    modify_time = db.Column(db.DateTime, default=Datetime.now, onupdate=datetime.now)

# birthday record
class Birthday(db.Model):
    __tablename__ = 'birthday'
    id = db.Column(db.String(30), primary_key=True, default=lambda: 'b_'+shortuuid.uuid())
    recorder_id = db.Column(db.String(30), db.ForeignKey('user.id'), nullable=False)
    recorder = db.relationship('User', backref=db.backref('birthday_records', lazy='dynamic'))
    date = db.Column(db.DateTime, nullable=False)