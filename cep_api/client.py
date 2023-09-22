import requests
import json

def get_cep(uf, estado, logradouro):
    url = f'https://viacep.com.br/ws/{uf}/{estado}/{logradouro}/json/'
    response = requests.get(url)
    response = response.json()
    return response
