import unittest
import time
from flask import url_for
from urllib.request import urlopen

from os import getenv
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from application import app, db, bcrypt
from application.models import Users, Events, Groups
from datetime import datetime
test_admin_user_name = "admin"
test_admin_email = "admin@email.com"
test_admin_password = "admin2020"


class TestBase(LiveServerTestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///data.db",
            SECRET_KEY="TEST_SECRET_KEY",
            DEBUG=True,
            TESTING=True
        )
        return app

    def setUp(self):
        """Setup the test driver and create test users"""
        print("--------------------------NEXT-TEST----------------------------------------------")
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium-browser"
        chrome_options.add_argument('--headless')
        chrome_options.add_argument("--remote-debugging-port=9222")
        chrome_options.add_argument("–no-sandbox")
        self.driver = webdriver.Chrome(
            executable_path=getenv('CHROMEDRIVER_PATH'), chrome_options=chrome_options)
        self.driver.get("http://localhost:5000")
        db.drop_all()
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
        self.driver.quit()
        print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")


class TestUserForms(TestBase):

    def test_registration(self):
        self.driver.find_element_by_xpath(
            "/html/body/div/form/a").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div/form/input[2]').send_keys(test_admin_user_name)
        self.driver.find_element_by_xpath('/html/body/div/form/input[3]').send_keys(
            test_admin_email)
        self.driver.find_element_by_xpath('/html/body/div/form/input[4]').send_keys(
            test_admin_password)
        self.driver.find_element_by_xpath('/html/body/div/form/input[5]').send_keys(
            test_admin_password)
        self.driver.find_element_by_xpath(
            '/html/body/div/form/input[6]').click()
        time.sleep(1)
        users = Users.query.all()
        user = Users.query.filter_by(user_name=test_admin_user_name).first()
        print(user)
        assert user in users
        assert url_for('home') in self.driver.current_url

    def test_login(self):
        self.driver.find_element_by_xpath(
            '/html/body/div/form/input[2]').send_keys('user1')
        self.driver.find_element_by_xpath(
            '/html/body/div/form/input[3]').send_keys('password')
        self.driver.find_element_by_xpath(
            '/html/body/div/form/input[4]').click()
        time.sleep(1)
        assert url_for('home') in self.driver.current_url

    def test_update_user(self):
        self.driver.find_element_by_xpath(
            '/html/body/div/form/input[2]').send_keys('user1')
        self.driver.find_element_by_xpath(
            '/html/body/div/form/input[3]').send_keys('password')
        self.driver.find_element_by_xpath(
            '/html/body/div/form/input[4]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div/nav/ul[2]/li/a').click()
        time.sleep(1)
        user = self.driver.find_element_by_xpath(
            '/html/body/div/div[1]/div/h1').text
        email = self.driver.find_element_by_xpath(
            '/html/body/div/div[1]/div/h3').text
        self.driver.find_element_by_xpath(
            '/html/body/div/nav/ul[2]/li/a').click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div/form/input[2]').clear()
        self.driver.find_element_by_xpath(
            '/html/body/div/form/input[2]').send_keys('user_1-updated')
        self.driver.find_element_by_xpath(
            '/html/body/div/form/input[3]').clear()
        self.driver.find_element_by_xpath(
            '/html/body/div/form/input[3]').send_keys('updated@email.test')
        self.driver.find_element_by_xpath(
            '/html/body/div/form/input[4]').click()
        time.sleep(1)

        assert url_for('view_user') in self.driver.current_url
        new_user = self.driver.find_element_by_xpath(
            '/html/body/div/div[1]/div/h1').text
        new_email = self.driver.find_element_by_xpath(
            '/html/body/div/div[1]/div/h3').text
        assert new_user != user
        assert new_email != email

    def test_log_out(self):
        self.driver.find_element_by_xpath(
            '/html/body/div/form/input[2]').send_keys('user1')
        self.driver.find_element_by_xpath(
            '/html/body/div/form/input[3]').send_keys('password')
        self.driver.find_element_by_xpath(
            '/html/body/div/form/input[4]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div/nav/ul[2]/li/a').click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/div/a[2]').click()
        time.sleep(1)
        assert url_for('login') in self.driver.current_url

    def test_delete_user(self):
        self.driver.find_element_by_xpath(
            '/html/body/div/form/input[2]').send_keys('user1')
        self.driver.find_element_by_xpath(
            '/html/body/div/form/input[3]').send_keys('password')
        user = Users.query.filter_by(user_name='user1')
        self.driver.find_element_by_xpath(
            '/html/body/div/form/input[4]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div/nav/ul[2]/li/a').click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/div/a[1]').click()
        time.sleep(1)
        users = Users.query.all()
        assert url_for('login') in self.driver.current_url
        assert user not in users


class TestEventForms(TestBase):
    def test_add_event(self):
        self.driver.find_element_by_xpath(
            '/html/body/div/form/input[2]').send_keys('user1')
        self.driver.find_element_by_xpath(
            '/html/body/div/form/input[3]').send_keys('password')
        self.driver.find_element_by_xpath(
            '/html/body/div/form/input[4]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div/nav/ul[1]/li/a').click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div/form/input[2]').send_keys('tester event')
        self.driver.find_element_by_xpath(
            '/html/body/div/form/input[3]').send_keys('tester event')
        self.driver.find_element_by_xpath(
            '/html/body/div/form/input[4]').send_keys('11/08/2020')
        self.driver.find_element_by_xpath(
            '/html/body/div/form/input[5]').click()
        time.sleep(1)
        assert url_for('home') in self.driver.current_url
        event_text = self.driver.find_element_by_xpath(
            '/html/body/div/table/tbody/tr[2]/td[1]').text
        assert event_text == 'tester event'


if __name__ == '__main__':
    unittest.main(port=5000)
