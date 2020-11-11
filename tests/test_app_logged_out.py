from tests.test_base import TestBase
from flask import url_for
from application import app, db, bcrypt
from application.models import Users, Groups, Events
from datetime import datetime
from flask_login import login_user, current_user, logout_user, login_required, login_manager


class TestViewsLoggedIn(TestBase):
    def test_get_index_logged_out(self):
        res = self.client.get(url_for('login'), follow_redirects=True)
        print(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'Login', res.data)

    def test_get_register_logged_out(self):
        res = self.client.get(url_for('register'), follow_redirects=True)
        print(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'New User', res.data)
