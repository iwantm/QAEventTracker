from application import app, db, bcrypt
from flask import render_template, redirect, url_for, request
from application.forms import RegistrationForm, LoginForm
from application.models import Users
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/')
def home():

    if current_user.is_authenticated:
        current = Users.query.filter_by(id=current_user.id).first()
        return current.user_name
    else:
        return 'logged out'


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pass = bcrypt.generate_password_hash(form.password.data)
        new_user = Users(
            user_name=form.user_name.data,
            email=form.email.data,
            password=hashed_pass
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('register.html', title='New User', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(user_name=form.user_name.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.stay_logged_in.data)
            return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return(redirect(url_for('home')))


@app.route('/user/delete')
@login_required
def delete_account():
    user_id = current_user.id
    user = Users.query.filter_by(id=user_id).first()
    logout_user()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('home'))
