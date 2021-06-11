from flask import url_for
from flask_testing import TestCase

from app2.app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestPowerCall(TestBase):
    def test_app2(self):
        response = self.client.get(url_for('elevation'))
        list_angles = "20,30,40,50,60,70, 80"
        self.assert200(response)
        self.assertIn(response.data.decode('utf-8'), list_angles)
