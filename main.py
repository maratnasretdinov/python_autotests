import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '7e4cdec8aaa9580a77c65b7d9064a1d1'
HEADER = {'Content-Type':'application/JSON', 'trainer_token': TOKEN}
TRAINER_ID = '7568'

body_new_pokemon = { # боди для нового покемона
    "name": "generate", 
    "photo_id": -1
    }

 body_pokemon_knockout = { # ввод id покемона, который отправляется в нокаут
    "pokemon_id": "123265"
    }

body_rename_pokemon = { # боди для переименования покемона
    "pokemon_id": "123264",
    "name": "generate",
    "photo_id": -1
}

body_pokemon_catch = { # боди для ловли покемона в покеболл
    "pokemon_id": "123264"
}

# при необходимости отправить покемона в нокаут
#response_pokemon_knockout = requests.post(url = f'{URL}/pokemons/knockout', headers = HEADER, json = body_pokemon_knockout)
#print(response_pokemon_knockout.text)


# запрос на создание покемона
response_new_pokemon = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_new_pokemon)
pokemon_id = response_new_pokemon.json()['id']
print(response_new_pokemon.text)


# запрос cмена имени покемона
response_rename_pokemon = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_rename_pokemon)
print(response_rename_pokemon.text)

# запрос на поимку покемона в покеболл
response_pokemon_catch = requests.post(url = f'{URL}/pokemons/trainers/add_pokeball', headers = HEADER, json = body_pokemon_catch)
print(response_pokemon_catch.text)