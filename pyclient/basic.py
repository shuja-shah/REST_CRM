import requests

ENDPOINT= 'http://localhost:8000/api/'

GET_RESPONE= requests.get(ENDPOINT, json={"name": "shuja"})

print(GET_RESPONE.text)
print(GET_RESPONE.json)