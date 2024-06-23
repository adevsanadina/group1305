import requests

url = "http://api.open-notify.org/astros.json"
response = requests.get(url)
data = response.json()


print("Astronauts:")
for astronaut in data["people"]:
    print(astronaut["name"])


new_url = "https://dummyjson.com/users"
new_response = requests.get(new_url)
new_data = new_response.json()


print("Users aged 28:")
for user in new_data["users"]:
    if user["age"] == 28:
        print(user["firstName"], user["lastName"])
