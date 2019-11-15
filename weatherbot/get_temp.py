#!/usr/bin/env python

import requests

def get_weather(city, api_token):
    url = "https://api.openweathermap.org/data/2.5/weather?q={},RU&appid={}".format(city, api_token)
    response = requests.get(url).json()
    temp = int(response["main"]["temp"])
    return temp

def conv_farh_to_cels(fahr):
    cels = int((fahr - 32) * 5/9)
    return round(cels)

def add_C(cels):
    return (cels + "°C").encode('utf-8')
