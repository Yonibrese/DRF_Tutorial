import requests

endpoint = "http://localhost:8000/api/products/6/update/"

data = {
    "title": "item 6.2",
    "price": 56.99
    }

get_response = requests.put(endpoint, json=data)

print(get_response.json())