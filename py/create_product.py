import json
import requests

url = 'https://api.robolabs.lt/api/create_product'

params = {
    "secret": "SECRET",
    "execute_immediately": True,
    "name": "New Product Name",
    "type": "product",
    "default_code": "PROD0002",
    "barcode": "978020137962",
    "vat_code": "PVM1",
    "categ_id": 4,
    "price": 15.0,
    "sync_price": True,
    "price_with_vat": 18.0
}

resp = requests.post(url=url, json=params)
data = resp.json()
print(data)
