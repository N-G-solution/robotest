import json
import requests

url = 'https://api.robolabs.lt/api/product_categories'

params = {
    "secret": "SECRET",
    "execute_immediately": True,
}

resp = requests.post(url=url, json=params)
data = resp.json()
print(len(data))
with open('product_categories.json', 'w') as txtfile:
    json.dump(data, txtfile)
