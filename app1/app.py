from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import random
import requests
from os import getenv

app = Flask(__name__)
db = SQLAlchemy(app)

service2 = 'http://serv2 :5002'
service3 = 'http://serv3:5003'
service4 = 'http://serv4:5004'


app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')

class record_fires(db.Model):
    id              = db.Column(db.Integer,     primary_key=True)
    velocity        = db.Column(db.Integer,     nullable=False)
    elevation       = db.Column(db.Integer,     nullable=False)
    result          = db.Column(db.Integer,     nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fire', methods=['GET','POST'])
def home():
    # Get data from App2 and App3
    velocity    = requests.get(service2)
    elevation   = requests.get(service3)
    data    = [power.text, angle.text]
    single = ','.join(data)
    outcome = requests.post(service4, data=single)
    new_kick = Newoutcomes(kick_power=power.text, kick_angle=angle.text, kick_outcome=outcome.text)
    db.session.add(new_kick)
    db.session.commit()
    return render_template('home.html', power=power, angle=angle, outcome=outcome) 


if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
