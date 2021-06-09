from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from flask_sqlalchemy import SQLAlchemy
import requests_mock
from os import getenv

from app1.app import app, db

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///", SECRET_KEY='TEST_SECRET_KEY', DEBUG=True, WTF_CSRF_ENABLED=False )
        return app 

    def setUp(self): 
        db.create_all()

    def tearDown(self): 
        db.session.remove() 
        db.drop_all()

class TestFire(TestBase):
    def test_home(self):
        response = self.client.get(url_for('index'))
        self.assert200(response)

    def test_fire(self):
        with requests_mock.mock() as p:
            p.get('http://app2:5002', text="45")
            p.get('http://app3:5003', text='99')
            p.post('http://app4:5004', text="Cannon Ball Simulator")
            
            response = self.client.post(url_for('fire'))
            self.assertIn(b'Cannon Ball Simulator', response.data)
