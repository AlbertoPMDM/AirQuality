import configparser
import json

config = configparser.ConfigParser(allow_no_value=True)

def ValueId(value):

    if value >= 0 and value <=50:
        quality = 'good'
    elif value > 50 and value <=100:
        quality = 'moderate'
    elif value > 100 and value <=150:
        quality = 'sensitive'
    elif value > 150 and value <=200:
        quality = 'unhealthy'
    elif value > 200 and value <=300:
        quality = 'veryunhealthy'
    elif value > 300 and value <=400:
        quality = 'hazardous1'
    elif value > 400 and value <=500:
        quality = 'hazardous2'
    
    return quality

config['Room Size'] = {
    '# Set the values to match the height, depth, and width of the room the sensor will be in (m3)' :None,
    'RoomHeight': '1',
    'RoomWidth': '1',
    'RoomDepth' : '1'
    }

config['Exposure Limits'] = {
    '# Adjusted for sick people': None,
    '# These are the recommended exposure limits for each contaminant (ug/m3 and ppm)': None,
    'pm25': '8.6',
    'pm10': '263',
    'co': '0.4'
    'co2': '500'
}
with open("AirData.json") as file:
    data = json.load(file)

    airquality= {
        '# Change this option only if you have custom values for contamination (WAQI scale)': None,
        '# Current status: ': ValueId(data['airquality']['pm25'])
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