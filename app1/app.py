from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import random
import requests
from os import getenv
from sqlalchemy import desc

app = Flask(__name__)
db = SQLAlchemy(app)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fire.db'
app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DATABASE_URI")

app2    = 'http://app2:5002'
app3    = 'http://app3:5003'
app4    = 'http://app4:5004'

class record_fires(db.Model):
    id              = db.Column(db.Integer,     primary_key=True)
    velocity        = db.Column(db.Integer,     nullable=False)
    elevation       = db.Column(db.Integer,     nullable=False)
    result          = db.Column(db.String(200), nullable=False)
 


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fire', methods=['GET','POST'])
def fire():
    # Get data from App2 and App3
    elevation_angle = requests.get(app2)
    muzzle_velocity = requests.get(app3)

    # Build into data to send to App4
    data            = [elevation_angle.text, muzzle_velocity.text]
    single          = ','.join(data)

    # Get result back
    result = requests.post(app4, data=single)

    # Query Database before adding
    all_firings = record_fires.query.with_entities(record_fires.result).order_by(desc(record_fires.id)).limit(10).all()

    # Write to database
    firing = record_fires(velocity=muzzle_velocity.text, elevation=elevation_angle.text, result=result.text)
    db.session.add(firing)
    db.session.commit()
    
    return render_template('index.html', velocity=muzzle_velocity, elevation=elevation_angle, outcome=result, allfires=all_firings) 


if __name__=='__main__': app.run(host='0.0.0.0', port=5000, debug=True)
