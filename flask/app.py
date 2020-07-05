from flask import Flask
from flask import Flask , redirect , url_for, render_template , request, session, flash, jsonify,make_response
import json
import random
app = Flask(__name__)

app.secret_key="webooster"

mockData = [
    {'time' : 1, 'temperature' : 0, 'altitude': 0, 'acceleration': 0 , 'latitude' : 0 , 'longitude' : 0},
    {'time' : 2, 'temperature' : 10, 'altitude': 100, 'acceleration': 10 , 'latitude' : 0 , 'longitude' : 0},
    {'time' : 3, 'temperature' : 20, 'altitude': 200, 'acceleration': 20 , 'latitude' : 0 , 'longitude' : 0},
    {'time' : 4, 'temperature' : 30, 'altitude': 300, 'acceleration': 30 , 'latitude' : 0 , 'longitude' : 0},
    {'time' : 5, 'temperature' : 40, 'altitude': 400, 'acceleration': 40 , 'latitude' : 0 , 'longitude' : 0},
    {'time' : 6, 'temperature' : 50, 'altitude': 500, 'acceleration': 50 , 'latitude' : 0 , 'longitude' : 0},
    {'time' : 7, 'temperature' : 60, 'altitude': 600, 'acceleration': 50 , 'latitude' : 0 , 'longitude' : 0},
    {'time' : 8, 'temperature' : 60, 'altitude': 700, 'acceleration': 60 , 'latitude' : 0 , 'longitude' : 0},
    {'time' : 9, 'temperature' : 55, 'altitude': 800, 'acceleration': 70 , 'latitude' : 0 , 'longitude' : 0},
    {'time' : 10, 'temperature' : 50, 'altitude': 900, 'acceleration': 80 , 'latitude' : 0 , 'longitude' : 0},
    {'time' : 11, 'temperature' : 40, 'altitude': 750, 'acceleration': 70 , 'latitude' : 0 , 'longitude' : 0},
    {'time' : 12, 'temperature' : 30, 'altitude': 300, 'acceleration': 60 , 'latitude' : 0 , 'longitude' : 0},
    {'time' : 13, 'temperature' : 20, 'altitude': 200, 'acceleration': 50 , 'latitude' : 0 , 'longitude' : 0},
    {'time' : 14, 'temperature' : 5, 'altitude': 100, 'acceleration': 20 , 'latitude' : 0 , 'longitude' : 0},

]

@app.route('/main')
def mainPage():
    return render_template('launchPage.html')

@app.route('/')
def boot():
    return render_template('bootstrap.html')

@app.route('/data', methods=["GET", "POST"])
def data():
    x = random.randint(0,13)
    print(x)
    data = mockData[x]
    response = make_response(json.dumps(data))

    response.content_type = 'application/json'

    return response

app.config['TEMPLATES_AUTO_RELOAD'] = True
if app == "__main__":
    app.run()
