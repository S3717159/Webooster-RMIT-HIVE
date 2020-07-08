from flask import Flask
from flask import Flask , redirect , url_for, render_template , request, session, flash, jsonify,make_response
import json
import random
import time

app = Flask(__name__)

app.secret_key="webooster"

mockData = [
    {'time' : 1, 'temperature' : 1, 'altitude': 1, 'acceleration': 1 , 'latitude' : 0 , 'longitude' : 0},
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
currentIndex = 0
previousData = {'time' : 1, 'temperature' : 1, 'altitude': 1, 'acceleration': 1 , 'latitude' : 0 , 'longitude' : 0}
currentData = mockData[currentIndex]
dataChange = {'temperatureChange' : 1, 'altitudeChange': 1, 'accelerationChange': 1 }


@app.route('/main')
def mainPage():
    return render_template('launchPage.html')

@app.route('/')
def boot():
    return render_template('bootstrap.html')

@app.route('/data', methods=["GET", "POST"])
def data():
    global dataChange
    global currentData
    data = Merge(dataChange, currentData)
    response = make_response(json.dumps(data))

    response.content_type = 'application/json'

    return response

@app.route('/updater', methods=["GET", "POST"])
def updater():
    while True:
        print('updating' )
        global currentData
        global currentIndex
        global previousData
        if currentIndex == 14:
            currentIndex = 0
        dataChangeUpdate()
        previousData = currentData
        currentData = mockData[currentIndex]
        currentIndex = currentIndex + 1
        time.sleep(1)
    
   
    
    

app.config['TEMPLATES_AUTO_RELOAD'] = True
if app == "__main__":
    app.run(threaded=True)


def dataChangeUpdate():
    global currentData
    global previousData
    global dataChange

    temperatureChange = calculateChange(previousData['temperature'],currentData['temperature'] )
    altitudeChange = calculateChange(previousData['altitude'],currentData['altitude'] )
    accelerationChange = calculateChange(previousData['acceleration'],currentData['acceleration'] )
    
    dataChange['temperatureChange'] = temperatureChange
    dataChange['altitudeChange'] = altitudeChange
    dataChange['accelerationChange'] = accelerationChange

def calculateChange(new, old):
    
    change = ((old - new )/old) * 100
    
    return round(change, 2)


def Merge(dict1, dict2): 
    res = {**dict1, **dict2} 
    return res 