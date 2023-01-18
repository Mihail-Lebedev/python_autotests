import requests
import json
token = 'f81bf7679f6bd2771d1440d64532889f'
response = requests.post('https://pokemonbattle.me:5000/pokemons', headers = {'Content-Type' : 'application/json',
  'trainer_token' : token},
json = {
    "name": "Бульба121ззз",
     "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
 })
print(response.text)

pokemon_id = response.json()['id']

response_change = requests.put('https://pokemonbattle.me:5000/pokemons', headers = {'Content-Type' : 'application/json',
  'trainer_token' : token}, json = {
    "pokemon_id": pokemon_id,
    "name": "Girafffff",
    "photo": ""
})
print(response_change.text)

response_add = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball', headers = {'Content-Type' : 'application/json',
  'trainer_token' : token},
json = {
    "pokemon_id": pokemon_id
})

print(response_add.text)