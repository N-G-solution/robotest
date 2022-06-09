import json
import requests

url = 'https://api.robolabs.lt/api/get_api_job'

params = {
    "secret": "SECRET",
    "api_job_id": 23419,
    "execute_immediately": True,
}
resp = requests.post(url=url, json=params)
data = resp.json()
print(data)
