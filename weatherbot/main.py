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

def main():
    if len(sys.argv) == 2:
        program_name = sys.argv[0]
        city = sys.argv[1]
    else:
        print("Please, enter the city")

if __name__ == '__main__':
     main()
