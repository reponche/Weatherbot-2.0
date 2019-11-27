import telegram
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
    chat_id = data["result"][-1]["message"]["chat"]["id"]
    message_text = data["result"][-1]["message"]["text"]

    message = {"chat_id": chat_id,
                "text": message_text}
    return message

def send_message(chat_id, text):
    url = URL + "sendMessage?chat_id={}&text={}".format(chat_id, text)
    requests.get(url)
