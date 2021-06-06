from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestPowerCall(TestBase):
    def test_app4(self):
        response = self.client.post(url_for('fire'), data='45,110')
        expected = "Muzzel Velocity=110 Elevation=45 Distance Travelled=1234 : Overshot - LOSER!"
        self.assert200(response)
        self.assertEqual(response.data.decode('utf-8'), expected)
        