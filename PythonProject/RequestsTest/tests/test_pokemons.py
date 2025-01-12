import requests
import pytest

URL ='https://api.pokemonbattle.ru/v2'
TOKEN = '6897e52289dd14fbb734a66dd2df594a'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '21048'

def test_status_code():
    response = requests.get(url=f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID })
    assert response.status_code == 200
def test_piece_body():
    response_piece_body = requests.get(url=f'{URL}/trainers', params= {'trainer_id': TRAINER_ID})
    assert response_piece_body.json()["data"][0]['trainer_name'] == 'Хайрбек'