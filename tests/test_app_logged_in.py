from tests.test_base import TestBase
from flask import url_for
from application import app, db, bcrypt
from application.models import Users, Groups, Events
from datetime import datetime
from flask_login import login_user, current_user, logout_user, login_required, login_manager


class TestLoggedIn(TestBase):
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

    def test_update_account_post(self):
        with self.client:
            log = self.client.get(url_for('auto_login'))
            old_un = current_user.user_name
            old_email = current_user.email
            res = self.client.post(
                url_for("update_user"),
                data=dict(user_name="update_user_1", email="test@test.test"),
                follow_redirects=True
            )
            all_users = Users.query.all()
            self.assertIn(current_user, all_users)
            self.assertNotEqual(old_un, current_user.user_name)
            self.assertNotEqual(old_email, current_user.email)

    def test_update_account_get(self):
        with self.client:
            log = self.client.get(url_for('auto_login'))
            res = self.client.get(
                url_for("update_user"))
            print(res.data)
            username = current_user.user_name
            test_string1 = 'value="'+username+'"'
            test_string2 = 'value="'+current_user.email+'"'
            self.assertIn(str.encode(test_string1), res.data)
            self.assertIn(str.encode(test_string2), res.data)

    def test_create_event(self):
        with self.client:
            log = self.client.get(url_for('auto_login'))
            res_get = self.client.get(
                url_for("create_event"))
            res = self.client.post(
                url_for("create_event"),
                data=dict(title="new test event", description="this is a test",
                          date="12/11/2020"),
                follow_redirects=True
            )
            new_event = Events.query.filter_by(title="new test event").first()
            all_events = Events.query.all()
            new_group = Groups.query.filter_by(
                user_id=current_user.id,
                event_id=new_event.id
            ).first()
            all_groups = Groups.query.all()
            self.assertIn(new_event, all_events)
            self.assertIn(new_group, all_groups)
            self.assertIn(b'Home', res.data)
            self.assertIn(b'Add Event', res_get.data)

    def test_delete_event(self):
        with self.client:
            log = self.client.get(url_for('auto_login'))
            all_events_before = Events.query.all()
            group = Groups.query.filter_by(user_id=current_user.id).first()
            event = Events.query.filter_by(id=group.event_id).first()
            res = self.client.get(
                url_for("delete_event", id=event.id),
                follow_redirects=True)
            all_events_after = Events.query.all()
            self.assertIn(event, all_events_before)
            self.assertNotIn(event, all_events_after)
            self.assertIn(b'Home', res.data)

    def test_update_event_post(self):
        with self.client:
            log = self.client.get(url_for('auto_login'))
            group = Groups.query.filter_by(user_id=current_user.id).first()
            event = Events.query.filter_by(id=group.event_id).first()
            old_title = event.title
            old_description = event.description
            old_date = event.date
            res = self.client.post(
                url_for("edit_event", id=event.id),
                data=dict(title="Event1_updated",
                          description="desc1_updated", date=datetime(2020, 12, 15, 00, 00, 00),
                          follow_redirects=True
                          ))
            updated_event = Events.query.filter_by(id=group.event_id).first()
            all_events = Events.query.all()
            self.assertNotEqual(updated_event.title, old_title)
            self.assertNotEqual(updated_event.description, old_description)
            self.assertNotEqual(updated_event.date, old_date)
            self.assertIn(updated_event, all_events)

    def test_update_event_get(self):
        with self.client:
            log = self.client.get(url_for('auto_login'))
            group = Groups.query.filter_by(user_id=current_user.id).first()
            event = Events.query.filter_by(id=group.event_id).first()
            res = self.client.get(
                url_for("edit_event", id=event.id))
            print(res.data)
            event_title = event.title
            event_description = event.description
            test_string1 = 'value="'+event_title+'"'
            test_string2 = 'value="'+event_description+'"'
            self.assertIn(str.encode(test_string1), res.data)
            self.assertIn(str.encode(test_string2), res.data)
