import requests
import json


api_url = "http://api.open-notify.org/astros.json"
response = requests.get(api_url)
data = response.json()


with open("astros.json", mode="w") as json_file:
    json.dump(data, json_file, indent=4)

