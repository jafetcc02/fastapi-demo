import requests

url = "http://127.0.0.1:8000/items"
data = {"text": "banana"}
response = requests.post(url, json=data)
print(response.json())