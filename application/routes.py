from application import app, db, bcrypt
from flask import render_template, redirect, url_for, request
from application.models import Users, Events, Groups
from application.forms import EventForm, RegistrationForm, LoginForm, UpdateAccountForm, EditEventForm, AddUserForm
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/')
@app.route('/home')
@login_required
def home():
    events = Groups.query.filter_by(
        user_id=current_user.id).join(Events).order_by(Events.date).all()
    return render_template('index.html', title='Home', events=events)

# User Routes


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if request.method == 'POST' or form.validate_on_submit():
        hashed_pass = bcrypt.generate_password_hash(form.password.data)
        new_user = Users(
            user_name=form.user_name.data.lower(),
            email=form.email.data,
            password=hashed_pass
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('home'))
    return render_template('register.html', title='New User', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()

    if request.method == "POST" or form.validate_on_submit():
        app.logger.info('submit' + form.password.data)
        user = Users.query.filter_by(user_name=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            app.logger.info('oof')
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
    group = Groups.query.filter_by(user_id=user_id).all()
    for event in group:
        event_table = Events.query.filter_by(id=event.event_id).first()
        db.session.delete(event)
        db.session.delete(event_table)

    logout_user()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/user/update', methods=['GET', 'POST'])
@login_required
def update_user():
    form = UpdateAccountForm()
    if request.method == 'POST' or form.validate_on_submit():
        current_user.user_name = form.user_name.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('view_user'))
    elif request.method == 'GET':
        form.user_name.data = current_user.user_name
        form.email.data = current_user.email

    return render_template('edit_user.html', title='Edit Account', form=form)


@app.route('/user', methods=['GET'])
@login_required
def view_user():
    account = Users.query.get(current_user.id)
    return render_template('view_user.html', title='My Account', account=account)

# Event Routes


@app.route('/event/create', methods=['GET', 'POST'])
@login_required
def create_event():
    form = EventForm()
    if request.method == 'POST' or form.validate_on_submit():
        new_event = Events(
            title=form.title.data,
            description=form.description.data,
            date=form.date.data
        )
        db.session.add(new_event)
        db.session.commit()
        new_group = Groups(
            user_id=current_user.id,
            event_id=new_event.id
        )
        db.session.add(new_group)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('new_event.html', title='Add Event', form=form)


@app.route('/event/delete/<int:id>')
@login_required
def delete_event(id):
    current = Events.query.get(id)
    group = Groups.query.filter_by(event_id=id).all()
    for group in group:
        db.session.delete(group)
    db.session.delete(current)
    db.session.commit()
    return(redirect(url_for('home')))


@app.route('/event/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_event(id):
    form = EditEventForm()
    current = Events.query.get(id)
    if request.method == 'POST' or form.validate_on_submit():
        current.title = form.title.data
        current.description = form.description.data
        current.date = form.date.data
        db.session.commit()
        return redirect(url_for('event_view', id=id))
    elif request.method == 'GET':
        form.title.data = current.title
        form.description.data = current.description
        form.date.data = current.date
    return render_template('new_event.html', title='Edit Event', form=form)


@app.route('/event/<int:id>')
@login_required
def event_view(id):
    event = Groups.query.filter_by(
        user_id=current_user.id,
        event_id=id
    ).first()
    if event:
        return render_template('view_event.html', title=event.events.title, event=event)
    else:
        return redirect(url_for('home'))


@app.route('/event/add/user/<int:id>', methods=['GET', 'POST'])
@login_required
def add_user(id):
    form = AddUserForm()
    event = Groups.query.filter_by(
        user_id=current_user.id,
        event_id=id
    ).first()

    if event:
        if request.method == 'POST' or form.validate_on_submit():
            add_user = Users.query.filter_by(
                user_name=form.user_name.data).first()
            new_group = Groups(
                user_id=add_user.id,
                event_id=id
            )
            db.session.add(new_group)
            db.session.commit()
            return redirect(url_for('event_view', id=id))
    else:
        return redirect(url_for('home'))
    return render_template('add_user_event.html', title=event.events.title, form=form)
