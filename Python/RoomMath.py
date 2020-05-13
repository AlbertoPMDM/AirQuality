import configparser
import json

config = configparser.ConfigParser()

config.read('../config.ini')

ConversionValues = {
    'good':{
        'aqi':{
            'ilow':0,
            'ihigh':50
        },
        'pm25':{
            'clow':0.0,
            'chigh':12.0
        },
        'pm10':{
            'clow': 0,
            'chigh':54
        },
        'co':{
            'clow':0.0,
            'chigh':4.4
        }
    },
    'moderate':{
        'aqi':{
            'ilow':51,
            'ihigh':100
        },
        'pm25':{
            'clow':12.1,
            'chigh':35.4
        },
        'pm10':{
            'clow':55,
            'chigh':154
        },
        'co':{
            'clow':4.5,
            'chigh':9.4
        }
    },
     'sensitive':{
        'aqi':{
            'ilow':101,
            'ihigh':150
        },
        'pm25':{
            'clow':35.5,
            'chigh':55.4
        },
        'pm10':{
            'clow':155,
            'chigh':254
        },
        'co':{
            'clow':9.5,
            'chigh':12.4
        }
    },
     'unhealthy':{
        'aqi':{
            'ilow':151,
            'ihigh':200
        },
        'pm25':{
            'clow':55.5,
            'chigh':150.4
        },
        'pm10':{
            'clow':255,
            'chigh':354
        },
        'co':{
            'clow':12.5,
            'chigh':15.4
        }
    },
     'veryunhealthy':{
        'aqi':{
            'ilow':201,
            'ihigh':300
        },
        'pm25':{
            'clow':150.5,
            'chigh':250.4
        },
        'pm10':{
            'clow':355,
            'chigh':424
        },
        'co':{
            'clow':15.5,
            'chigh':30.4
        }
    },
     'hazardous1':{
        'aqi':{
            'ilow':301,
            'ihigh':400
        },
        'pm25':{
            'clow':250.5,
            'chigh':350.4
        },
        'pm10':{
            'clow':425,
            'chigh':504
        },
        'co':{
            'clow':30.5,
            'chigh':40.4
        }
    },
    'hazardous2':{
        'aqi':{
            'ilow':401,
            'ihigh':500
        },
        'pm25':{
            'clow':350.5,
            'chigh':500.4
        },
        'pm10':{
            'clow':505,
            'chigh':604
        },
        'co':{
            'clow':40.5,
            'chigh':50.4
        }
    }
}

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

def conversion(ihigh, ilow, chigh, clow, i):
    result = (((chigh-clow)/(ihigh-ilow) ) * (i-ilow))+ clow
    return result

def AqiToUnit(aqi, type, convval = ConversionValues):
    quality = ValueId(aqi)
    SetValues = convval[quality]
    iaqi = SetValues['aqi']
    contaminant = SetValues[type]
    result = conversion(iaqi['ihigh'], iaqi['ilow'], contaminant['chigh'], contaminant['clow'], aqi)
    return  round(result, 2)
    

def getRoomSize():
    height = config.getfloat('Room Size','roomheight')
    width = config.getfloat('Room Size', 'roomwidth')
    depth = config.getfloat('Room Size', 'roomdepth')
    size = [height, width, depth]
    return size

def RoomVol():
    size = getRoomSize()
    vol = size[0] * size[1] * size[2]
    return vol

def RoomVolLiters():
    vol = RoomVol()
    liters = vol * 1000
    return liters

def getPm25():
    aqipm25 = config.getfloat('Air Quality', 'pm25')
    pm25 = AqiToUnit(aqipm25, 'pm25')
    return pm25

def getPm10():
    aqipm10 = config.getfloat('Air Quality', 'pm10')
    pm10 = AqiToUnit(aqipm10, 'pm10')
    return pm10

def getCo():
    aqico = config.getfloat('Air Quality', 'co')
    co = AqiToUnit(aqico, 'co')
    return co

def getCo2():
    return 400

def getIndividualPm25():
    ug = 1.4
    pm25_per_person = ug/RoomVol()
    return round(pm25_per_person, 2)

def getIndividualCo2():
    mg = 700000
    co_per_person =  mg/RoomVolLiters()
    return round(co_per_person, 2)

def getPm25Limit():
    difference = config.getfloat('Exposure Limits', 'pm25') - getPm25()
    if difference <= 0:
        limit = 0
    elif difference > 0:
        limit = int(difference/getIndividualPm25())
    return limit

def getCo2Limit():
    difference = config.getfloat('Exposure Limits', 'co2') - getCo2()
    if difference <= 0:
        limit = 0
    elif difference > 0:
        limit = int(difference/getIndividualCo2())
    return limit

def chooser():
    if getCo2Limit() > getPm25Limit():
        choice = getPm25Limit()
    elif getPm25Limit() == getCo2Limit():
        choice = getPm25Limit()
    elif getCo2Limit() < getPm25Limit():
        choice = getCo2Limit()
    return choice

limit = {'limit': str(chooser())}

with open("PersonLimit.json", "w") as file:
    json.dump(limit, file)

