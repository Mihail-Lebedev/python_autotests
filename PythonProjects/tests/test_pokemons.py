import requests
import pytest

def test_status_cde():
    response =requests.get('https://pokemonbattle.me:5000/trainers')
    assert response.status_code == 200

@pytest.mark.parametrize('key, value', [('trainer_name', 'mikhail'),('city' ,'samara')])

def test_parametr(key,value):
    response =requests.get('https://pokemonbattle.me:5000/trainers', params = {'trainer_id' : '1808'})
    assert response.json()[key] == value
