import unittest
from flask import url_for
import flask_login
from flask_testing import TestCase

from application import app, db, bcrypt, test_routes
from application.models import Users, Groups, Events
from datetime import datetime
from flask_login import login_user, current_user, logout_user, login_required, login_manager


class TestBase(TestCase):
    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
        app.config.update(
            SECRET_KEY="TEST_SECRET_KEY",
            DEBUG=True,
            TESTING=True
        )
        return app

    def setUp(self):
        db.create_all()
        new_user1 = Users(user_name='user1',
                          email='user1@user.com',
                          password=bcrypt.generate_password_hash('password'))
        new_user2 = Users(user_name='user2',
                          email='user2@user.com',
                          password=bcrypt.generate_password_hash('password2'))
        new_event1 = Events(title='Event1',
                            description='desc1',
                            date=datetime(2020, 12, 13, 00, 00, 00))
        new_event2 = Events(title='Event2',
                            description='desc2',
                            date=datetime(2020, 12, 13, 00, 00, 00))
        db.session.add(new_user1)
        db.session.add(new_user2)
        db.session.add(new_event1)
        db.session.add(new_event2)
        db.session.commit()
        new_group1 = Groups(user_id=new_user1.id,
                            event_id=new_event1.id)
        new_group2 = Groups(user_id=new_user2.id,
                            event_id=new_event2.id)
        db.session.add(new_group1)
        db.session.add(new_group2)

        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
