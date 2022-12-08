from app import app
from app import db

from flask import render_template
from flask import redirect
from flask import url_for

from app.models import UserModel

from app.forms import SignupForm
from app.forms import SigninForm
from app.forms import ProfileSettingsForm

from flask_login import current_user
from flask_login import logout_user
from flask_login import login_user
from flask_login import login_required

from werkzeug.utils import secure_filename
import os


@app.route('/')
def view_mainpage():
    return render_template("mainpage_template.html")


@app.route('/signin/', methods=['GET', 'POST'])
def view_signin():
    if current_user.is_authenticated:
        return redirect(url_for('view_mainpage'))
    else:
        form_1 = SigninForm()
        if form_1.validate_on_submit():
            user_username = UserModel.query.filter_by(username=form_1.username_or_email.data).first()
            user_email = UserModel.query.filter_by(email=form_1.username_or_email.data).first()
            if user_email is None:
                if user_username is None:
                    return redirect(url_for('view_signin'))
                else:
                    if user_username.check_password(form_1.password.data):
                        login_user(user_username, remember=form_1.remember_me.data)
                        return redirect(url_for("view_mainpage"))
                    else:
                        return redirect(url_for('view_signin'))
            else:
                if user_email.check_password(form_1.password.data):
                    login_user(user_email, remember=form_1.remember_me.data)
                    return redirect(url_for("view_mainpage"))
                else:
                    return redirect(url_for('view_signin'))
        else:
            return render_template('signin_template.html', form=form_1)


@app.route('/signup/', methods=['GET', 'POST'])
def view_signup():
    if current_user.is_authenticated:
        return redirect(url_for('view_signin'))
    else:
        form_1 = SignupForm()
        if form_1.validate_on_submit():
            user = UserModel(username=form_1.username.data, email=form_1.email.data)
            user.set_password(form_1.password.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('view_signin'))
        else:
            return render_template("signup_template.html", form=form_1)


@app.route('/logout/')
def view_logout():
    logout_user()
    return redirect(url_for('view_mainpage'))


@app.route('/profile/')
def view_profile():
    return "Your profile"


@login_required
@app.route('/profile/settings/', methods=['GET', 'POST'])
def view_profile_settings():
    form_1 = ProfileSettingsForm()
    if form_1.validate_on_submit():
        if current_user.first_name != form_1.first_name.data:
            current_user.first_name = form_1.first_name.data
        if current_user.last_name != form_1.last_name.data:
            current_user.last_name = form_1.last_name.data
        if current_user.phone_number != form_1.phone_number.data:
            current_user.phone_number = form_1.phone_number.data
        if current_user.sending_recommendations != form_1.sending_recommendations.data:
            current_user.sending_recommendations = form_1.sending_recommendations.data
        if current_user.sending_messages != form_1.sending_messages.data:
            current_user.sending_messages = form_1.sending_messages.data
        if form_1.avatar.data:
            file = form_1.avatar.data
            path = "static/uploads/" + str(current_user.username) + "/avatars/avatar.png"
            file.save(path)
            file.close()
        db.session.commit()
        return redirect(url_for('view_profile'))
    else:
        return render_template("profile_settings_template.html", form=form_1)


@app.route('/serbia/')
def view_mainpage_serbia():
    return "Main page serbia"

