import os
import yaml
from yaml.loader import SafeLoader
from flask import Flask, request, render_template
from services.db_utils import DBUtils
from flask import request
import requests


app = Flask(__name__)
app.debug = True
cf_port = os.getenv("PORT")

@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/weather',methods=['POST','GET'])
def get_weather_info():

    dbUtils = DBUtils()
    db_connection = dbUtils.connect_to_db()

    if request.method == 'POST':
        new_city_name = request.form.get('city')
        dbUtils.add_city_to_db(db_connection,'info','city',new_city_name)


    cities = dbUtils.fetch_all_cities(db_connection,'info','city')


    with open('./properties.yaml') as f:
        properties = yaml.load(f, Loader=SafeLoader)
    url = properties['Weather'].get('URL')

    weather_data = []

    for city in cities:
        r = requests.get(url.format(city.city_name)).json()

        weather = {
            'city': city.city_name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }

        weather_data.append(weather)

    return render_template('weatherinfo.html', weather_data=weather_data)


if __name__ == '__main__':

    if cf_port is None:
        app.run(host='0.0.0.0', port=5000, debug=True)
    else:
        app.run(host='0.0.0.0', port=int(cf_port), debug=True)
