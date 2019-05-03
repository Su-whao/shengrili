from flask import Flask 
from db import db
from models import User, Birthday
import config

app = Flask(__name__)

app.config.form_object(config)

db.init_app(app)


if __name__ == '__main__':
    app.run()