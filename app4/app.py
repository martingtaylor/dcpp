from flask import Flask, request, Response
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import math

app = Flask(__name__)
target_distance = 1000

def source_result(distance_traveled):
    if distance_traveled == target_distance:
        result = "Good Shot - Bulls Eye!"
    else:
        dt = abs(target_distance - int(distance_traveled))

        if dt > 0 and dt <= 10:
            result = "Within 10 meters - Good Shot!"
        elif dt > 10 and dt <= 20:
            result = "Within 20 meters - Good Shot!"
        elif dt > 20 and dt <= 30:
            result = "Within 30 meters - Not Bad!"
        elif dt > 30 and dt <= 40:
            result = "Within 40 meters - Not Bad!"
        elif dt > 40 and dt <= 50:    
            result = "Within 50 meters - Try Again!"
        elif dt > 50 and dt <= 60:
            result = "Within 60 meters - Try Again!"
        elif dt > 60 and dt <= 70:
            result = "Within 70 meters - Way Off!"
        elif dt > 70 and dt <= 80:
            result = "Within 80 meters - Way Off!"
        elif dt > 80 and dt <= 90:
            result = "Within 90 meters - Bad Bad!"
        elif dt > 90 and dt <= 100:
            result = "Within 100 meters - Bad Shot!"   
        else:
            if distance_traveled > target_distance:
                result = "Overshot - LOSER!"
            else:
                result = "Undershot - LOSER!"

    return result


@app.route('/', methods=['GET'])
def fire():
	# Get request details
    text = request.data.decode("utf-8")
	
	# Decode request to list and parse to elevation and muzzle_velocity
    #fire_details 	= list(text.split(','))
    #elevation 		= int(fire_details[0])
    #muzzle_velocity	= int(fire_details[1])
	
	# Calculate distance cannon bull travels
    elevation = 45
    muzzle_velocity = 110 # 90 - 110

    # Convert degress to radians
    angle_radians = math.radians(elevation)
    
    # Distance calculation
    accelreation_due_to_gravity = 9.8

    distance_traveled = int(math.sin(2 * angle_radians) * muzzle_velocity**2 / accelreation_due_to_gravity)


    result = source_result(distance_traveled)
    

    return  "Muzzel Velocity=" + \
            str(muzzle_velocity) + \
            " Elevation=" + str(elevation) + \
            " Distance Travelled=" + str(distance_traveled) + \
            " : " + result

    '''
    if power >= 50:
        data1 = 'It\'s a powerful kick, stright past the endzone... and thats game. YOU LOOSE'
        return Response( data1, mimetype='text/plain')
    elif power in range (25,50):
        if angle in range (45,136):
            data1 = 'The kick goes stright to the kick returner, who takes a knee... game over. YOU LOOSE'
            return Response( data1, mimetype='text/plain')
        else: 
            data1 = 'The angle looked good Bob, but just too much power... and that wraps up this game. YOU LOOSE'
            return Response( data1, mimetype='text/plain')
    elif power <= 24:
        if angle in range (45) or angle in range (136,180):
            data1 = 'This kick looks good Bob, a nice low drive... wait... I think Barkely\'s got it, he evades one tackle, it\'s a stright footrace now... TOUCHDOWN!! YOU WIN'
            return Response( data1, mimetype='text/plain')
        else:
            data1 = 'Well that kick sums up their game Bob, flat, and no purpose...it\'s over. YOU LOOSE'
            return Response( data1, mimetype='text/plain')
    '''

if __name__ == '__main__':
    app.run(debug=True, port=5004, host='0.0.0.0')
