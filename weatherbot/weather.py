import requests

from weatherbot.tokens import OWM_TOKEN

OWM_URL = "https://api.openweathermap.org/data/2.5/weather?q={},RU&appid={}"

def get_weather(city):
    url = OWM_URL.format(city, OWM_TOKEN)
    response = requests.get(url).json()
    return response

def get_temp(response):
    """Get a temperature from OWM reponse, or None if response is 'city wasn't found'"""
    try:
        return int(response["main"]["temp"])
    except KeyError:
        return None

def conv_kelv_to_cels(temp):
    return round(int(temp - 273.15))

def add_C(cels):
    return str(cels) + u"\xb0C"
