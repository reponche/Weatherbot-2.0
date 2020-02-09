#!/usr/bin/env python3

# Hack to add weatherbot to sys.path for proper imports
import sys
from os.path import dirname, abspath
curdir = abspath(dirname(dirname(__file__)))
sys.path.insert(0,curdir)

import time

from weatherbot.weather import get_weather, conv_kelv_to_cels, add_C, get_temp
from weatherbot.tokens import OWM_TOKEN
from weatherbot.telegram import get_updates, send_message
from weatherbot.puller import Puller


def parse_cli(args):
    try:
        input = int(sys.argv[1])
    except ValueError:

        if len(sys.argv) == 2:
            weather = get_weather(sys.argv[1], OWM_TOKEN)
            temp = conv_kelv_to_cels(weather)
            cels = add_C(temp)
            print(cels)

        if len(sys.argv) > 2:
            print("Please, enter the one parameter. For example: Moscow")

    except IndexError:
        print("Please, enter the city")

    else:
        print("Please, enter the city, not numbers. For example: Moscow")

def get_response(message):
    chat_id = message["message"]["chat"]["id"]
    message_text = message["message"]["text"]
    response = get_weather(message_text)
    temp = get_temp(response)
    return chat_id, temp, message_text


def main():
    puller = Puller("./puller_state")
    while True:
        time.sleep(5)
        updates = get_updates()
        if updates['ok'] != True:
            print(f"Something happened, too bad. Response was: {updates}")
            sys.exit(1)
        results = updates['result']
        puller.pull(results)
        latest = puller.get_elems()

        for message in latest:
            (chat_id, temperature, city) = get_response(message)

            if temperature is None:
                send_message(chat_id, f"I don't have information about this city. Are you sure {city} is a city?")
            else:
                cels = conv_kelv_to_cels(temperature)
                weather = add_C(cels)
                send_message(chat_id, f"{weather} in {city}")


if __name__ == '__main__':
     main()
