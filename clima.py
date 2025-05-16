import urllib.request
import json
import datetime


def weatherInformation (data):
    #print(data)
    print(f"Este es el clima en la ciudad {data['name']} es {data['weather'][0]['main']}")
    print(f"La temperatura es de : {data['main']['temp']}° C.")
    print(f"A las {convertTime(data['sys']['sunrise'],data['timezone'])} amanecera.")
    print(f"A las {convertTime(data['sys']['sunset'],data['timezone'])} se pondra de noche.")
    

def convertTime(cTime,timeZone):
    #timeZone = timeZone/3600
    cityTime = datetime.datetime.fromtimestamp(cTime)
    uthTime = datetime.datetime.time(cityTime)
    # print(uthTime)
    #newTime = datetime.datetime.time(times)
    return uthTime

#def weatherEmoji(weather):


def obtener_clima(ciudad, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"
    #print(url)
    with urllib.request.urlopen(url) as response:
        jsData= response.read()
        #print(data)
        data = json.loads(jsData)
        #print(jsonData)
        weatherInformation(data)


def weatherCity ():

    print("-"*30)

    city = input("Ingrese la ciudad que desea consultar: ")
    obtener_clima(city, "bb9db544a062b278fb1dead2057fbbd5")



weatherCity()

