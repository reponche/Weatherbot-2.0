import requests
from weatherbot.tokens import OWN_TOKEN

def get_weather(city, OWN_TOKEN):
    url = "https://api.openweathermap.org/data/2.5/weather?q={},RU&appid={}".format(city, OWN_TOKEN)
    response = requests.get(url).json()
    temp = int(response["main"]["temp"])
    return temp

def conv_kelv_to_cels(temp):
    cels = int(temp - 273.15)
    return round(cels)

def add_C(cels):
    return (str(cels) + u"\xb0C")
