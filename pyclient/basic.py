import requests

ENDPOINT= 'http://localhost:8000/api/'

GET_RESPONE= requests.get(ENDPOINT, params={'username': 'Shuja'})

print(GET_RESPONE.status_code)
print(GET_RESPONE.json)
print(GET_RESPONE.text)