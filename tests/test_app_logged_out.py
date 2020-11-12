from tests.test_base import TestBase
from flask import url_for
from application import app, db, bcrypt
from application.models import Users, Groups, Events
from datetime import datetime
from flask_login import login_user, current_user, logout_user, login_required, login_manager


class TestLoggedOut(TestBase):
    def test_get_index_logged_out(self):
        res = self.client.get(url_for('login'), follow_redirects=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'Login', res.data)

    def test_get_register_logged_out(self):
        res = self.client.get(url_for('register'), follow_redirects=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'New User', res.data)

    def test_log_in(self):
        res = self.client.post(
            url_for("login"),
            data=dict(username="user1", password="password"),
            follow_redirects=True
        )
        res_no_rd = self.client.post(
            url_for("login"),
            data=dict(username="user1", password="password")
        )
        self.assertIn(b'Home', res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_no_rd.status_code, 302)

    def test_register(self):
        res = self.client.post(
            url_for("register"),
            data=dict(user_name="test1", email="test@test.test",
                      password="password", confirm_password="password"),
            follow_redirects=True
        )
        self.assertIn(b'Home', res.data)
        self.assertEqual(res.status_code, 200)
