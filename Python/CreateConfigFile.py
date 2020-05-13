import configparser
import json

config = configparser.ConfigParser(allow_no_value=True)

config['Room Size'] = {
    '# Set the values to match the height, depth, and width of the room the sensor will be in (m3)' :None,
    'RoomHeight': '1',
    'RoomWidth': '1',
    'RoomDepth' : '1'
    }

config['Exposure Limits'] = {
    '# These are the recommended exposure limits for each contaminant': None,
    'pm25': '25',
    'pm10': '50',
    'co': '35'
}
with open("AirData.json") as file:
    data = json.load(file)

    airquality= {
        '# Change this option only if you have custom values for contamination (WAQI scale)': None
    }
    airquality.update(data['airquality'])

    config['Air Quality'] = airquality

    location = {
        '# This is the location from which the Air Quality data is from': None
    }
    location.update(data['location'])

    config['Location'] = location


with open("../config.ini", "w") as configfile:
    config.write(configfile)