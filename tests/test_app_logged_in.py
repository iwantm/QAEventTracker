from tests.test_base import TestBase
from flask import url_for
from application import app, db, bcrypt
from application.models import Users, Groups, Events
from datetime import datetime
from flask_login import login_user, current_user, logout_user, login_required, login_manager


class TestViewsLoggedIn(TestBase):
    def test_get_index_logged_in(self):
        with self.client:
            res = self.client.get(url_for('auto_login'))
            res = self.client.get(url_for('login'), follow_redirects=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn(b'Home', res.data)

    def test_get_register_logged_in(self):
        with self.client:
            res = self.client.get(url_for('auto_login'))
            res = self.client.get(url_for('register'), follow_redirects=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn(b'Home', res.data)

    def test_logout_logged_in(self):
        with self.client:
            res = self.client.get(url_for('auto_login'))
            res = self.client.get(url_for('logout'), follow_redirects=True)
            self.assertFalse(current_user.is_authenticated)
            self.assertEqual(res.status_code, 200)
            self.assertIn(b'Login', res.data)

    def test_delete_account(self):
        with self.client:
            res = self.client.get(url_for('auto_login'))
            group = Groups.query.filter_by(
                user_id=current_user.id).first()
            user_event = Events.query.filter_by(id=group.events.id).first()
            user = current_user
            all_users = Users.query.all()
            res = self.client.get(
                url_for('delete_account'), follow_redirects=True)
            all_groups = Groups.query.all()
            all_events = Events.query.all()

            self.assertNotIn(user, all_users)
            self.assertNotIn(group, all_groups)
            self.assertNotIn(user_event, all_events)
            self.assertNotIn(user, all_users)
            self.assertFalse(current_user.is_authenticated)
            self.assertEqual(res.status_code, 200)
            self.assertIn(b'Login', res.data)

    def test_event_view(self):
        with self.client:
            res = self.client.get(url_for('auto_login'))
            group = Groups.query.filter_by(
                user_id=current_user.id).first()
            user_event = Events.query.filter_by(id=group.events.id).first()
            res = self.client.get(
                url_for('event_view', id=user_event.id), follow_redirects=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn(str.encode(user_event.description), res.data)
            self.assertIn(str.encode(user_event.title), res.data)

    def test_event_view_doesnt_exist(self):
        with self.client:
            res = self.client.get(url_for('auto_login'))
            res = self.client.get(
                url_for('event_view', id=10), follow_redirects=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn(b'Home', res.data)

    def test_event_view_wrong_user(self):
        with self.client:
            res = self.client.get(url_for('auto_login'))
            res = self.client.get(
                url_for('event_view', id=2), follow_redirects=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn(b'Home', res.data)

    def test_view_user(self):
        with self.client:
            res = self.client.get(url_for('auto_login'))
            res = self.client.get(
                url_for('view_user'), follow_redirects=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn(str.encode(current_user.user_name), res.data)
            self.assertIn(str.encode(current_user.email), res.data)
