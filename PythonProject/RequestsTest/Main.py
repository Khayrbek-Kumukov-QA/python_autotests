import requests

URL ='https://api.pokemonbattle.ru/v2'
TOKEN = '6897e52289dd14fbb734a66dd2df594a'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}



body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_change = {
    "pokemon_id": "190615",
    "name": "Бульбазавр615",
    "photo_id": 2
}

body_pokeball = {
    "pokemon_id": "190615"
}

responce_create = requests.post(url=f'{URL}/pokemons',headers = HEADER,json = body_create)  
print(responce_create.json())


responce_put = requests.put(url=f'{URL}/pokemons',headers = HEADER,json = body_change)  
print(responce_put.json())

responce_pokeball = requests.post(url=f'{URL}/trainers/add_pokeball',headers = HEADER,json = body_pokeball)  
print(responce_pokeball.json())