from application import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(15), nullable=False, unique=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    group = db.relationship('Group', backref='users')


class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    date = db.Column(db.DateTime)
    group = db.relationship('Group', backref='events')


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column('users_id', db.Integer, db.ForeignKey('users.id'))
    event_id = db.Column('events_id', db.Integer, db.ForeignKey('events.id'))
