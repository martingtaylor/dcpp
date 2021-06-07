from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import random
import requests
from os import getenv

app = Flask(__name__)
db = SQLAlchemy(app)

app2    = 'http://app2:5002'
app3    = 'http://app3:5003'
app4    = 'http://app4:5004'


app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')

#class record_fires(db.Model):
#    id              = db.Column(db.Integer,     primary_key=True)
#    velocity        = db.Column(db.Integer,     nullable=False)
#    elevation       = db.Column(db.Integer,     nullable=False)
#    result          = db.Column(db.String,      nullable=False)
 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fire', methods=['GET','POST'])
def home():
    # Get data from App2 and App3
    muzzle_velocity = requests.get(service2)
    elevation_angle = requests.get(service3)

    # Build into data to send to App4
    data            = [elevation_angle.text, muzzle_velocity.text]
    single          = ','.join(data)

    # Get result back
    result = requests.post(service4, data=single)

    # Write to database
    # firing = record_fires(velocity=muzzle_velocity.text, elevation=elevation_angle.text, result=reuslt.text)
    # db.session.add(firing)
    # db.session.commit()

    return render_template('index.html', velocity=muzzle_velocity, angle=elevation_angle, outcome=result) 


if __name__=='__main__': app.run(host='0.0.0.0', port=5000, debug=True)
