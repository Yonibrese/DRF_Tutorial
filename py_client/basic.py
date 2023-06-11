import requests

endpoint = "http://localhost:8000/api/"


get_response = requests.get(endpoint, json={"Query": "Hello world"})
print(get_response.json())
# print(get_response.headers)
# print(get_response.text)