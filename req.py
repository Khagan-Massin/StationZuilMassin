#Massin Elotmani
import requests
import json
def temp_req(stad):
    """
    Pakt de temperatuur van OpenWeatherAPI
    :param Een stad in Nederland met een treinstation (Te vinden in station_lijst)
    :return: De temperatuur in die locatie in Celsius
    """
    resource_uri = f"https://api.openweathermap.org/data/2.5/weather?q={stad.lower()}&appid=623674843eb5b413c214a36bad8eefdc"
    response = requests.get(resource_uri)
    response_data = response.json()
    weer = response_data['main']
    return round((float(weer['temp']) - 273.15), 1)

def weer_icon(stad):
    """
    Pakt het juiste weer icon van OpenWeatherAPI
    :param Een stad in Nederland met een treinstation (Te vinden in station_lijst):
    :return: een 2 cijfer en 1 letter code komt over met de naam van een png bestand in StationZuilMassin/weather_icons
    (code + @2x.png = naam)
    """
    resource_uri = f"https://api.openweathermap.org/data/2.5/weather?q={stad.lower()}&appid=623674843eb5b413c214a36bad8eefdc"
    response = requests.get(resource_uri)
    response_data = response.json()
    boek = ((response_data['weather'])[0])
    return boek['icon']
#Zorgt voordat de test niet tijdens de import word gedraaid.
if __name__ == "__main__":
    print(temp_req('tilburg'))
    print(weer_icon('tilburg'))
# Test de api's