import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "This is a BS Title",
    "content": "This is a BS content",
    "price": 42.89
}

get_response = requests.post(endpoint, json=data)

print(get_response.json())