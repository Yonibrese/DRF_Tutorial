import requests

endpoint = "http://localhost:8000/api/"


get_response = requests.post(endpoint, json={"title": "hello world", "content": "this is some stuff"})
print(get_response.json())
# print(get_response.headers)
# print(get_response.text)