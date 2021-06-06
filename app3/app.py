from flask import Flask, request, Response
import random

app = Flask(__name__)

@app.route('/', methods=['GET'])
def velocity():
    muzz_vel = str(random.randrange(90, 110))
    # return Response(muzz_vel, mimetype='type/plain')
    return muzz_vel

if __name__== '__main__': app.run(debug=True, port=5003, host='0.0.0.0')
