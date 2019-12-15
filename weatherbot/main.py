#!/usr/bin/env python3

import sys
from os.path import dirname, abspath
curdir = abspath(dirname(dirname(__file__)))
sys.path.insert(0,curdir)

import requests
import json
from weatherbot.get_temp import get_weather, conv_kelv_to_cels, add_C
from weatherbot.tokens import OWN_TOKEN
from weatherbot.telegram import get_updates, get_message, get_update_id, send_message

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
    while True:
        data = get_updates()
        message_text = get_message(data)
        print(message_text)

if __name__ == '__main__':
     main()
