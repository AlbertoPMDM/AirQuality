import configparser
import json

config = configparser.ConfigParser(allow_no_value=True)

config.read('../config.ini')

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

with open('../config.ini', 'w') as configfile:
    config.write(configfile)