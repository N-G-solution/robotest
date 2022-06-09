import json
import requests

url = 'https://api.robolabs.lt/api/get_invoice'

params = {
    "secret": "SECRET",
    "invoice_id": 786,
    "invoice_number": "TEST-14789",
    "invoice_reference": "TEST-14789",
    "partner_code": "378965478",
    "execute_immediately": True,
}

resp = requests.post(url=url, json=params)
data = resp.json()
print(len(data))
with open('get_invoice.json', 'w') as txtfile:
    json.dump(data, txtfile)
