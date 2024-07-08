import requests

url = 'https://script.google.com/macros/s/AKfycbwrCvZVCnLPNhESBuiXHAfckSC2T18c3-zRzZPGeW31PVtCakCGDeHp8w5u6iD0E0r9/exec'

def get_zoo_data() -> dict:
    response = requests.get(url, timeout=5)
    data = response.json()
    return data

def get_african_animals(zoo_data: dict):
    result = {}
    result['amount_of_animals'] = 0
    result['continent'] = []
    for african_animal in zoo_data['animals']:
        if african_animal['continent'] == 'Африка':
            result['amount_of_animals'] += african_animal['amount_of_animals']
    print(f'Зараз африканьских тварин: {result}')


def main():
    zoo_data = get_zoo_data()
    african_animals_data = get_african_animals((zoo_data))

main()