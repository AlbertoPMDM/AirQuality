import json
import urllib.request
import configparser

def getIaqiData(req, file):
    value = file["data"]["iaqi"][req]["v"]
    return value

def getLocationData(req, file):
    value = file["data"]["city"][req]
    return value

def getTimeData(req, file):
    value = file["data"]["time"][req]
    return value

url = "https://api.waqi.info/feed/here/?token=f885b91d7f41be2daa0e2fde2fcb8b63c0f4cf52"

response = urllib.request.urlopen(url)

with response as x:
    data = json.loads(x.read())
    RequestedData = {
        'airquality':{
            'pm25':getIaqiData("pm25", data),
            'pm10':getIaqiData("pm10", data),
            'co':getIaqiData("co", data)
        },
        'location':{
            'coordinates':getLocationData("geo", data),
            'name':getLocationData("name", data)
        },
        'time':getTimeData("s", data),
        'timezone':getTimeData("tz", data)
    }
    with open("AirData.json", "w") as file:
        RequestedDataJson = json.dump(RequestedData, file, indent=4)

response.close()