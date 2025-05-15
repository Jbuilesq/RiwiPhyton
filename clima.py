import urllib.request
import json

def weatherPrint (data):
    #print(data)
    print(f"El clima en la ciudad {data['name']} es de : {data['main']['temp']} ° C ")


def obtener_clima(ciudad, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"

    #print(url)
    with urllib.request.urlopen(url) as response:
        data= response.read()
        #print(data)
        jsonData = json.loads(data)
        #print(jsonData)
        weatherPrint(jsonData)


def weatherCity ():
    #print("Selecciones una de las siguiente ciudades para consultar el clima")
    city = input("Ingrese la ciudad que desea consultar: ")
    obtener_clima(city, "bb9db544a062b278fb1dead2057fbbd5")



weatherCity()

