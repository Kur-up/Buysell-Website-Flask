from app import db
from app import login

from flask_login import UserMixin

from werkzeug.security import generate_password_hash, check_password_hash

import datetime


class CountryModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Country: {} | ID: {} >'.format(self.name, str(self.id))


class CityModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    country_id = db.Column(db.Integer, db.ForeignKey('country_model.id'))

    def __repr__(self):
        return '<City: {} | ID: {} | Country ID: {} >'.format(self.name, str(self.id), str(self.country_id))


class UserModel(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    email_validate = db.Column(db.Boolean, default=False)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))
    avatar = db.Column(db.String(128))
    phone_number = db.Column(db.String(32), index=True, unique=True)
    registration_timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    visiting_timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
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

    def get_avatar(self):
        path = "static/uploads/" + str(self.username) + "/avatars/" + str(self.avatar)
        return path


class PersonalItemsClothesModel(db.Model):
    # Required
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True)
    description = db.Column(db.String(1024))
    price = db.Column(db.Float)
    photo_list = db.Column(db.PickleType)
    city_id = db.Column(db.Integer, db.ForeignKey('city_model.id'))
    country_id = db.Column(db.Integer, db.ForeignKey('country_model.id'))
    owner_id = db.Column(db.Integer, db.ForeignKey('user_model.id'))
    create_timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    stop_timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow()+datetime.timedelta(days=30))
    active_status = db.Column(db.Boolean, default=True)
    deleted_status = db.Column(db.Boolean, default=False)
    like_count = db.Column(db.Integer, default=0)

    # Additional
    clothes_type = db.Column(db.String(32))
    clothes_season = db.Column(db.String(32))
    clothes_sex = db.Column(db.String(16))
    clothes_size = db.Column(db.String(8))
    clothes_status = db.Column(db.String(16))

    def __repr__(self):
        return '<Post-PersonalItemsClothes: Post ID: {} | Owner ID: {} >'.format(str(self.id), str(self.owner_id))

    def upload_photo:
        pass

    def get_photo:
        pass


@login.user_loader
def load_user(user_id):
    return UserModel.query.get(int(user_id))