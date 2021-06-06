from flask import Flask, request, Response
import random

app = Flask(__name__)

@app.route('/', methods=['GET'])
def elevation():
    angles = ["20", "30", "40", "50", "60", "70"]
    angle = random.choice(angles)
    return Response(angle, mimetype='type/plain')

if __name__== '__main__':
    app.run(debug=True, port=5002, host='0.0.0.0')
