from flask import url_for
from flask_testing import TestCase

from app3.app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestPowerCall(TestBase):
    def test_app3(self):
        response = self.client.get(url_for('velocity'))
        list_angles = "20,30,40,50,60,70"
        self.assert200(response)
        self.assertIn(response.data.decode('utf-8'), "90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110")
        