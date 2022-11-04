#Massin Elotmani
import requests
import json
def temp_req():
    resource_uri = "https://api.openweathermap.org/data/2.5/weather?q=amsterdam&appid=623674843eb5b413c214a36bad8eefdc"
    response = requests.get(resource_uri)
    response_data = response.json()
    weer = response_data['main']
    return round((float(weer['temp']) - 273.15), 2)

def weer_icon():
    resource_uri = "https://api.openweathermap.org/data/2.5/weather?q=amsterdam&appid=623674843eb5b413c214a36bad8eefdc"
    response = requests.get(resource_uri)
    response_data = response.json()
    boek = ((response_data['weather'])[0])
    return boek['icon']

if __name__ == "__main__":
    print(temp_req())
    print(weer_icon())

