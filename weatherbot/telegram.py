import requests
from weatherbot.tokens import TELEGRAM_TOKEN

URL = "https://api.telegram.org/bot" + TELEGRAM_TOKEN + "/"

def get_updates():
    # получаю обновления от сервера телеграм в виде словаря в формате json :
    url = URL + "getUpdates"
    response = requests.get(url)
    return response.json()

def get_message(data):
    # в словаре ищу id пользователя и его text, записываю их в переменные
    # и возвращаю себе словарь message, состоящий только из этих переменных, [-1] - чтобы взять последний элемент
    message_text = data["result"][-1]["message"]["text"]
    return message_text

def get_chat_id(data):
    chat_id = data["result"][-1]["message"]["chat"]["id"]
    return chat_id

def get_update_id(data):
    update_id = data["result"][-1]["update_id"]
    return update_id

def send_message(chat_id, text):
    url = URL + "sendMessage?chat_id={}&text={}".format(chat_id, text)
    requests.get(url)
