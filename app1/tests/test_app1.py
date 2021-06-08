from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from flask_sqlalchemy import SQLAlchemy
import requests_mock
import sqlalchemy as db
from os import getenv

from app1.app import app 

class TestBase(TestCase):
    def create_app(self):
        return app 


class TestFire(TestBase):
    def test_fire(self):
        with requests_mock.mock() as p:
            p.get('http://app2:5002', text="45")
            p.get('http://app3:5003', text='99')
            p.post('http://app4:5004', text="Cannon Ball Simulator")
            
            response = self.client.post(url_for('fire'))
            self.assertIn(b'Cannon Ball Simulator', response.data)
