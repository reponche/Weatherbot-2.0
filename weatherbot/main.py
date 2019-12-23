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
    i = 0
    while True:
        data = get_updates()
        chat_id = get_chat_id(data)
        update_id = get_update_id(data)
        message_text = get_message(data)
        response = get_weather(message_text)
        temp = get_temp(response)

        if update_id == i:

            if temp == None:
                send_message(chat_id, "I don't have information about this city. Are you sure this is a city?")

            else:
                cels = conv_kelv_to_cels(temp)
                weather = add_C(cels)
                send_message(chat_id, "{} in {}".format(weather, message_text))

        i = update_id + 1

if __name__ == '__main__':
     main()
