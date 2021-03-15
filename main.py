from flask import Flask, request
from flask_cors import CORS, cross_origin
import requests

app = Flask(__name__)
CORS(app, support_credentials=True)

# app.run(debug=True) 

@app.route('/weather', methods=['GET'])
@cross_origin(supports_credentials=True)
def getWeatherForecast():
    # get city parameter
    city = request.args.get('city') + ",br" if request.args.get('city') else None
    lat = request.args.get('lat') if request.args.get('lat') else None
    lon = request.args.get('lon') if request.args.get('lon') else None

    # http://api.openweathermap.org/data/2.5/forecast?lat=-5.037560099999999&lon=-42.7564573&lang=pt_br&units=metric&appid=aaa1129fc07f4aacb6763552a1f84c0b

    querystring = {
        "q": city, 
        "lat": lat, 
        "lon": lon,
        "lang": "pt_br", 
        "units": "metric", 
        "appid": "aaa1129fc07f4aacb6763552a1f84c0b"
    }

    r = requests.get(
        url = 'http://api.openweathermap.org/data/2.5/forecast',
        params = querystring
    )
    json_object = r.json()
    return json_object
