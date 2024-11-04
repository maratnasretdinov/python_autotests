import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '7e4cdec8aaa9580a77c65b7d9064a1d1'
HEADER = {'Content-Type':'application/JSON', 'trainer_token': TOKEN}
TRAINER_ID = '7568'

def test_trainer_status_code(): # тест на получение ответа со статусом 200
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id':TRAINER_ID})
    assert response.status_code == 200

def test_trainer_id(): # тест на соответствие id тренера
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id':TRAINER_ID})
    assert response.json()['data'][0]['id'] == '7568'