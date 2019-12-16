#!/usr/bin/env python3

import sys
from os.path import dirname, abspath
curdir = abspath(dirname(dirname(__file__)))
sys.path.insert(0,curdir)

import requests
import json
from weatherbot.get_temp import get_weather, conv_kelv_to_cels, add_C
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
    data = get_updates()
    update_id = get_update_id(data)

    while True:
        data = get_updates()
        update_id = get_update_id(data)
        chat_id = get_chat_id(data)
        
        try:
            message_text = int(get_message(data))

        except ValueError:
            weather = get_weather(message_text, OWN_TOKEN)
            temp = conv_kelv_to_cels(weather)
            cels = add_C(temp)
            send_message(chat_id,cels)

        else:
            send_message(chat_id,"Please, enter the city, not numbers. For example: Moscow")

data = get_updates()
print(get_message(data))


if __name__ == '__main__':
     main()
