import time
import requests
import re
import json


class CryptoClass:
    def __init__(self, name):
        self.name = name.upper()
        self.cnt = 0
        self.html = []
        self.value_list = []
        self.price = 0.0
        self.last_price = 0.0

        self.update_price()
        self.last_price = self.price

    def update_price(self):
        self.html = requests.get('https://api.binance.com/api/v3/ticker/price')
        if self.html.status_code != 200:
            print('Internet connection lost')
            time.sleep(360)
        value_list_tmp = re.findall('{"symbol":"' + str(self.name) + 'USDP","price":"\d+\.\d+"', self.html.text)

        if value_list_tmp:
            self.value_list = re.findall('\d+\.\d+', value_list_tmp[0])
            self.price = float(self.value_list[0])

        else:
            btc = CryptoClass("BTC")
            btc.update_price()
            value_list_tmp = re.findall('{"symbol":"' + str(self.name) + 'BTC","price":"\d+\.\d+"', self.html.text)

            self.value_list = re.findall('\d+\.\d+', value_list_tmp[0])
            self.price = float(self.value_list[0])
            self.price *= btc.price


class CryptoClassUpdated:
    def __init__(self, name):
        self.name = name.upper()
        self.cnt = 0
        self.course = {}
        self.html = []
        self.price = 0.0
        self.last_price = 0.0

        self.update_price()
        self.last_price = self.price

    def update_price(self):
        html = requests.get('https://api.binance.com/api/v3/ticker/price')
        if html.status_code != 200:
            print('Internet connection lost')
            time.sleep(360)
        else:
            test = json.loads(html.text)
            for i in test:
                self.course[i['symbol']] = i['price']

            self.price = float(self.course[str(self.name) + "USDP"]) if str(self.name) + "USDP" in self.course.keys() else -1

            if self.price == -1:
                btc = CryptoClass("BTC")
                btc.update_price()

                self.price = float(self.course[str(self.name) + "BTC"])
                self.price *= btc.price