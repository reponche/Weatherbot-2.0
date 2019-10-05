import requests
import json

def get_updates():
    url = "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22nome%2C%20ak%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
    response = requests.get(url)
    return response.json()

def main():
    dictionary = get_updates()
    with open('yahoo.json', 'w') as jsonfile:
           json.dump(dictionary, jsonfile, indent=2, ensure_ascii=False)
    print(dictionary)

if __name__ == '__main__':
     main()
