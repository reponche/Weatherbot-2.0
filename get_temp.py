import requests

def get_weather():
    url = "https://api.openweathermap.org/data/2.5/weather?q=Moscow,RU&appid=da161f5c79219dcf1ea9677481ddd49a"
    response = requests.get(url).json()
    # temp = int(response["coord"]["lon"]["channel"]["item"]["condition"]["temp"])
    return response

def conv_farh_to_cels(fahr):
    cels = ((fahr - 32) * 5/9)
    return cels

def add_C(cels):
    temp = str(conv_farh_to_cels(cels)) + "℃"
    return temp
