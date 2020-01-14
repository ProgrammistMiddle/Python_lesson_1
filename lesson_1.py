import json
import requests

url = "https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11"
responce = requests.get(url)
data = json.loads(responce.text)
print(data)
print('ccy-код валюты')
print('base_ccy-Код национальной валюты')
print('buy-Курс покупки')
print('sale-Курс продажи')