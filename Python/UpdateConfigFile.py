import configparser
import json

config = configparser.ConfigParser(allow_no_value=True)

config.read('../config.ini')

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

with open('../config.ini', 'w') as configfile:
    config.write(configfile)