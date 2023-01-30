from bs4 import BeautifulSoup
import requests
import pandas as pd
import json
import time

cmc = requests.get("https://coinmarketcap.com/")
soup = BeautifulSoup(cmc.content, "html.parser")
# print("SOUP")
# print(soup.prettify())
data = soup.find('script', id="__NEXT_DATA__", type="application/json")
coins = {}

coin_data = json.loads(data.contents[0])
tmp = coin_data["props"]["initialState"]
# print(tmp[0:500])
tmpJson = json.loads(tmp)
# print(tmpJson.keys())
print("ICI")
# print(tmpJson["cryptocurrency"]["listingLatest"]["data"][1:])
data = tmpJson["cryptocurrency"]["listingLatest"]["data"][1:]

coin_name = []
coin_symbol = []
market_cap = []
percent_change_1h = []
percent_change_24h = []
percent_change_7d = []
price = []
volume_24h = []

for i in data:
    coin_name.append(i[13])
    coin_symbol.append(i[-4])
    price.append(i[5])
    percent_change_1h.append(
        i[20])
    percent_change_24h.append(
        i[21])
    percent_change_7d.append(
        i[24])
    market_cap.append(i[17])
    volume_24h.append(i[29])
print("price", price)
print('percent_change_1h', percent_change_1h)
print("percent_change_24h", percent_change_24h)
print("percent_change_7d", percent_change_7d)
print("market_cap", market_cap)
print("volume_24h", volume_24h)
