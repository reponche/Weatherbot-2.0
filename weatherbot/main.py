#!/usr/bin/env python3

import sys
# из модуля os.path, который расположен в модуле os достаю функции os.path.abspath() и os.path.dirname()
# первая укажет нам абсолютный путь, вторая укажет имя директории
from os.path import dirname, abspath
curdir = abspath(dirname(dirname(__file__)))
sys.path.insert(0,curdir)

import requests
import json
from weatherbot.get_temp import get_weather
from weatherbot.tokens import TELEGRAM_TOKEN

URL = "https://api.telegram.org/bot" + TELEGRAM_TOKEN + "/"

def get_updates():
    # получаю обновления от сервера телеграм в виде словаря в формате json :
    url = URL + "getUpdates"
    response = requests.get(url)
    return response.json()

def get_message():
    # в словаре ищу id пользователя и его text, записываю их в переменные
    # и возвращаю себе словарь message, состоящий только из этих переменных, [-1] - чтобы взять последний элемент
    data = get_updates()
    chat_id = data["result"][-1]["message"]["chat"]["id"]
    message_text = data["result"][-1]["message"]["text"]

    message = {"chat_id": chat_id,
                "text": message_text}
    return message

def send_message(chat_id, text):
    url = URL + "sendMessage?chat_id={}&text={}".format(chat_id, text)
    requests.get(url)

def main():
    # dictionary = get_updates()

    # with open("updates.json", "w", encoding='utf-8') as jsonfile:
    #      json.dump(dictionary, jsonfile, indent=2, ensure_ascii=False)
    # while True:
        answer = get_message()
        chat_id = answer["chat_id"]
        text = answer["text"]

        if '/start' in text:
            send_message(chat_id, "Hi, I can help you to know the weather, just tell me the city.")
        elif '/city' in text:
            send_message(chat_id, get_weather())
        else:
            send_message(chat_id, "If you want to know the weather just send me a city.")


if __name__ == '__main__':
     main()
