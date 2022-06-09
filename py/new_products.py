import json
import requests

url = 'https://api.robolabs.lt/api/new_products'

params = {
    "secret": "SECRET",
    "date_from": "2020-01-01 00:00:00",
    "date_to": "2023-01-31 00:00:00",
    "execute_immediately": True,
}

resp = requests.post(url=url, json=params)
data = resp.json()
print(len(data))
with open('new_products.json', 'w') as txtfile:
    json.dump(data, txtfile)