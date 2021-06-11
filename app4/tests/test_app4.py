from flask import url_for
from flask_testing import TestCase

from app4.app import app

class TestBase(TestCase):
    def create_app(self):
        return app

        
class TestPowerCall(TestBase):
    def test_app4(self):
        # Overshot
        response = self.client.post(url_for('fire'), data='45,110')
        self.assert200(response)
        expected = "Muzzle Velocity=110 Elevation=45 Distance Travelled=1234 : Overshot - LOSSER!"
        self.assertEqual(response.data.decode('utf-8'), expected)
        
        # Undershot
        response = self.client.post(url_for('fire'), data='45,89')
        self.assert200(response)
        expected = "Muzzle Velocity=89 Elevation=45 Distance Travelled=808 : Undershot - LOSSER!"
        self.assertEqual(response.data.decode('utf-8'), expected)        

        # Bulls Eye
        response = self.client.post(url_for('fire'), data='45,99')
        self.assert200(response)
        expected = "Muzzle Velocity=99 Elevation=45 Distance Travelled=1000 : Good Shot - Bulls Eye!"
        self.assertEqual(response.data.decode('utf-8'), expected)  

        # 10
        response = self.client.post(url_for('fire'), data='46,99')
        self.assert200(response)
        expected = "Muzzle Velocity=99 Elevation=46 Distance Travelled=999 : Within 10 meters - Good Shot!"
        self.assertEqual(response.data.decode('utf-8'), expected)

        # 20
        response = self.client.post(url_for('fire'), data='45,100')
        self.assert200(response)
        expected = "Muzzle Velocity=100 Elevation=45 Distance Travelled=1020 : Within 20 meters - Good Shot!"
        self.assertEqual(response.data.decode('utf-8'), expected)
        
        # 30
        response = self.client.post(url_for('fire'), data='45,98')
        self.assert200(response)
        expected = "Muzzle Velocity=98 Elevation=45 Distance Travelled=979 : Within 30 meters - Not Bad!"
        self.assertEqual(response.data.decode('utf-8'), expected)        

        # 40
        response = self.client.post(url_for('fire'), data='45,97')
        self.assert200(response)
        expected = "Muzzle Velocity=97 Elevation=45 Distance Travelled=960 : Within 40 meters - Not Bad!"
        self.assertEqual(response.data.decode('utf-8'), expected)  

        # 50
        response = self.client.post(url_for('fire'), data='46,97')
        self.assert200(response)
        expected = "Muzzle Velocity=97 Elevation=46 Distance Travelled=959 : Within 50 meters - Try Again!"
        self.assertEqual(response.data.decode('utf-8'), expected) 

        # 60
        response = self.client.post(url_for('fire'), data='45,96')
        self.assert200(response)
        expected = "Muzzle Velocity=96 Elevation=45 Distance Travelled=940 : Within 60 meters - Try Again!"
        self.assertEqual(response.data.decode('utf-8'), expected) 
        
        # 70
        response = self.client.post(url_for('fire'), data='46,96')
        self.assert200(response)
        expected = "Muzzle Velocity=96 Elevation=46 Distance Travelled=939 : Within 70 meters - Way Off!"
        self.assertEqual(response.data.decode('utf-8'), expected) 

        # 80
        response = self.client.post(url_for('fire'), data='45,95')
        self.assert200(response)
        expected = "Muzzle Velocity=95 Elevation=45 Distance Travelled=920 : Within 80 meters - Way Off!"
        self.assertEqual(response.data.decode('utf-8'), expected) 

        # 90
        response = self.client.post(url_for('fire'), data='43,95')
        self.assert200(response)
        expected = "Muzzle Velocity=95 Elevation=43 Distance Travelled=918 : Within 90 meters - Bad Bad!"
        self.assertEqual(response.data.decode('utf-8'), expected) 

        # 100
        response = self.client.post(url_for('fire'), data='45,94')
        self.assert200(response)
        expected = "Muzzle Velocity=94 Elevation=45 Distance Travelled=901 : Within 100 meters - Bad Shot!"
        self.assertEqual(response.data.decode('utf-8'), expected)         

