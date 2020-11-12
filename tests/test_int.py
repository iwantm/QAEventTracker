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

        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(
            executable_path="/home/iwantm/QA/chromedriver", chrome_options=chrome_options)
        self.driver.get("https://google.com")
        db.session.commit()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        self.driver.quit()
        print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")

    def test_server_is_up_and_running(self):
        response = urlopen("https://google.com")
        self.assertEqual(response.code, 200)


if __name__ == '__main__':
    unittest.main(port=5000)
