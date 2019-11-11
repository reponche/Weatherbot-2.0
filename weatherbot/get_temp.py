import requests

#def get_weather():
#    url = "https://api.openweathermap.org/data/2.5/weather?q=Moscow,RU&appid=da161f5c79219dcf1ea9677481ddd49a"
#    response = requests.get(url).json()
#    temp = int(response["coord"]["lon"]["channel"]["item"]["condition"]["temp"])
#    return response

fahr = 50

def conv_farh_to_cels(fahr):
    a = int((fahr - 32) * 5/9)
    cels = round(a)
    return cels

cels = str(conv_farh_to_cels(fahr))

def add_C(cels):
    temp = (cels + "°C").encode('utf-8')
    return temp

print(add_C(cels))
