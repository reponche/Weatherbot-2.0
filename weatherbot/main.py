#!/usr/bin/env python3

# Hack to add weatherbot to sys.path for proper imports
import sys
import json
from os.path import dirname, abspath
import os
curdir = abspath(dirname(dirname(__file__)))
sys.path.insert(0,curdir)

from weatherbot.weather import get_weather, conv_kelv_to_cels, add_C, get_temp
from weatherbot.telegram import get_updates, send_message
from weatherbot.state import State


def main():
    puller = State("./puller_state")
    owm_results = []
    if not os.path.exists("owm_results.json"):
        file = open("owm_results.json", 'x')

    while True:
        updates = get_updates()
        if updates["ok"] is False:
            print(f"Something happened, too bad. Response was: {updates}")
            sys.exit(1)
        results = updates['result']
        puller.filter(results)
        latest = puller.get_elems()

        for message in latest:
            chat_id = message["message"]["chat"]["id"]
            message_text = message["message"]["text"]
            response = get_weather(message_text)
            temp = get_temp(response)

            if temp is None:
                send_message(chat_id, f"I don't have information about this city. Are you sure {message_text} is a city?")
            else:
                cels = conv_kelv_to_cels(temp)
                weather = add_C(cels)
                send_message(chat_id, f"{weather} in {message_text}")
                owm_results.append(response)
                with open("owm_results.json", 'a') as file:
                    file.write(json.dumps(owm_results, indent=4))



if __name__ == '__main__':
    main()
