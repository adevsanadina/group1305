import requests

url = 'https://script.google.com/macros/s/AKfycbwrCvZVCnLPNhESBuiXHAfckSC2T18c3-zRzZPGeW31PVtCakCGDeHp8w5u6iD0E0r9/exec'

def get_zoo_data() -> dict:
    response = requests.get(url, timeout=5)
    data = response.json()
    return data

def get_toxic_animals(zoo_data: dict):
    result = {}
    result['amount_of_animals'] = 0
    result['toxiety'] = []
    for toxic_animal in zoo_data['animals']:
        result['amount_of_animals'] += toxic_animal['amount_of_animals']
        if toxic_animal['toxiety'] == True:
            count_of_toxic_animals = toxic_animal['amount_of_animals'] / toxic_animal['toxiety']
    print(f'Вартість догляду за отруйними тваринами: {count_of_toxic_animals}')

def main():
    zoo_data = get_zoo_data()
    toxic_animals_data = get_toxic_animals((zoo_data))


main()