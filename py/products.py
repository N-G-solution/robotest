import json
import requests

url = 'https://api.robolabs.lt/api/products'

params = {
    "secret": "SECRET",
    "warehouse": "WH",
    "execute_immediately": True,
}

resp = requests.post(url=url, json=params)
data = resp.json()
print(len(data))
with open('products.json', 'w') as txtfile:
    json.dump(data, txtfile)