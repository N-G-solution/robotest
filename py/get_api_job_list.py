import json
import requests

url = 'https://api.robolabs.lt/api/get_api_job_list'

params = {
    "secret": "SECRET",
    "date_from": "2020-01-01 00:00:00",
    "date_to": "2023-01-31 00:00:00",
    "state": "to_execute",
    "execute_immediately": True,
}

resp = requests.post(url=url, json=params)
data = resp.json()
print(data)
