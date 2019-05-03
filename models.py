
from db import db
from datetime import datetime
import shortuuid

# 用户
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.String(30), primary_key=True, default=lambda: 'u_'+shortuuid.uuid())
    openid = db.Column(db.String(50), nullable=False, unique=True, index=True)
    birthday = db.Column(db.Date)

    create_time = db.Column(db.DateTime, default=datetime.now)
    modify_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

# birthday record
class Birthday(db.Model):
    __tablename__ = 'birthday'
    id = db.Column(db.String(30), primary_key=True, default=lambda: 'b_'+shortuuid.uuid())
    recorder_openid = db.Column(db.String(30), db.ForeignKey('user.openid'), nullable=False)
    recorder = db.relationship('User', backref=db.backref('birthday_records', lazy='dynamic'))
    remark_name = db.Column(db.String(20))
    describe = db.Column(db.String(50))
    date = db.Column(db.Date, nullable=False)

    create_time = db.Column(db.DateTime, default=datetime.now)
    modify_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)