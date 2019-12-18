#!/usr/bin/env python3

import sys
from os.path import dirname, abspath
curdir = abspath(dirname(dirname(__file__)))
sys.path.insert(0,curdir)

import requests
import json
from weatherbot.get_temp import get_weather, conv_kelv_to_cels, add_C, get_temp
from weatherbot.tokens import OWN_TOKEN
from weatherbot.telegram import get_updates, get_message, get_update_id, send_message, get_chat_id

def parse_cli(args):
    try:
        input = int(sys.argv[1])
    except ValueError:

        if len(sys.argv) == 2:
            weather = get_weather(sys.argv[1], OWN_TOKEN)
            temp = conv_kelv_to_cels(weather)
            cels = add_C(temp)
            print(cels)

        if len(sys.argv) > 2:
            print("Please, enter the one parametr. For example: Moscow")

    except IndexError:
        print("Please, enter the city")

    else:
        print("Please, enter the city, not numbers. For example: Moscow")


def main():
    running = True

    while running:
        data = get_updates()
        chat_id = get_chat_id(data)
        message_text = get_message(data)
        response = get_weather(message_text)

#если город будет введен неверно, get_weather не найдет о нем данные на сервере OWM, в таком случае ф-ия не вернет словарь с данными, а get_temp не найдет погоду
#соответственно выведет None

        if get_temp(response) == None:
            send_message(chat_id, "I don't have information about this city. Are you sure this is a city?")
            running = False

        else:
            temp = get_temp(response)
            cels = conv_kelv_to_cels(temp)
            weather = add_C(cels)
            send_message(chat_id, weather)
            running = False


if __name__ == '__main__':
     main()
