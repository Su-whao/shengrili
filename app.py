from flask import Flask 
from db import db
from models import User, Birthday
import config

from apps.user.urls import user
from apps.birthday.urls import birthday

app = Flask(__name__)

app.config.from_object(config)

db.init_app(app)

app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(birthday, url_prefix='/birthday')


if __name__ == '__main__':
    app.run(host=0.0.0.0, port=5050)