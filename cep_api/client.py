import requests
import json

def get_cep(uf, cidade, logradouro):
    url = f'https://viacep.com.br/ws/{uf}/{cidade}/{logradouro}/json/'
    response = requests.get(url)
    response = response.json()
    return response
