import requests
from weatherbot.tokens import OWN_TOKEN

def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather?q={},RU&appid={}".format(city, OWN_TOKEN)
    response = requests.get(url).json()
    return response

#если город в сервисе openweathermap не находится, то сервис выдает словарь, в котором говорится о том, что сервис не нашел такого города
#структура словаря перестраивается и ф-ия get_temp не может найти погоду города, поэтому выкидывает ошибку KeyError, которую я использую для построения
#ответа пользователю

def get_temp(response):
    try:
        temp = response["main"]["temp"]
    except KeyError:
        return None
    else:
        return int(temp)

def conv_kelv_to_cels(temp):
    cels = int(temp - 273.15)
    return round(cels)

def add_C(cels):
    return (str(cels) + u"\xb0C")
