import requests

ENDPOINT= 'http://localhost:8000/api/'

GET_RESPONE= requests.post(ENDPOINT, json={
    'username': 'Dada_BABA',
    'email': 'FSM@example.com',
    'password': 'testInG',
})

print(GET_RESPONE.status_code)
print(GET_RESPONE.json)
print(GET_RESPONE.text)