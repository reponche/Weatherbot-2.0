import requests

from weatherbot.tokens import TELEGRAM_TOKEN

URL = "https://api.telegram.org/bot" + TELEGRAM_TOKEN + "/"

def get_updates():
    """получаю обновления от сервера телеграм в виде словаря в формате json"""
    url = URL + "getUpdates"
    response = requests.get(url)
    return response.json()


def send_message(chat_id, text):
    url = URL + "sendMessage?chat_id={}&text={}".format(chat_id, text)
    requests.get(url)
