from flask import url_for
from flask_testing import TestCase

from app3.app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestPowerCall(TestBase):
    def test_app3(self):
        response = self.client.get(url_for('velocity'))
        self.assert200(response)
        self.assertIn(int(response.data.decode('utf-8')), range(90,120))

        