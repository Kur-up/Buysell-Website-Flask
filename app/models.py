from app import db
from app import login

from flask_login import UserMixin

from werkzeug.security import generate_password_hash, check_password_hash

from datetime import datetime


class UserModel(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    email_validate = db.Column(db.Boolean, default=False)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))
    avatar = None
    phone_number = db.Column(db.String(32), index=True, unique=True)
    registration_timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    visiting_timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    rating = db.Column(db.Integer, default=0)
    banned = db.Column(db.Boolean, default=False)
    sending_recommendations = db.Column(db.Boolean, default=True)
    sending_messages = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return '<User: {} | ID: {} >'.format(self.username, str(self.id))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(user_id):
    return UserModel.query.get(int(user_id))