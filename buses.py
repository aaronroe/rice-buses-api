from flask import Flask
from werkzeug.contrib.cache import SimpleCache
import urllib2

app = Flask(__name__)

cache = SimpleCache()

@app.route("/")
def buses():
    return getBusData(), 200, {'Access-Control-Allow-Origin': '*'}

def getBusData():
    busData = cache.get('buses')
    if busData is None:
        busData = urllib2.urlopen("http://bus.rice.edu/json/buses.php").read()
        cache.set('buses', busData, timeout=5)
    return busData

if __name__ == "__main__":
    app.run()