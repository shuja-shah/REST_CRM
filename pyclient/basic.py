import requests

ENDPOINT= 'http://localhost:8000/api/'

GET_RESPONE= requests.get(ENDPOINT, json={"todo": "Read a book", })

print(GET_RESPONE.status_code)
print(GET_RESPONE.json)
print(GET_RESPONE.text)