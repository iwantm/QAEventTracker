from application import app, db, bcrypt
from flask import render_template, redirect, url_for, request
from application.forms import EventForm, RegistrationForm, LoginForm, UpdateAccountForm, EditEventForm
from application.models import Users, Events, Groups
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/test/auto_login')
def auto_login():
    user = (Users
            .query
            .filter_by(user_name="user1")
            .first())
    login_user(user, remember=True)
    return "ok"
