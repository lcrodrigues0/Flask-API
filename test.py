import requests

BASE = "http://127.0.0.1:5000/"

response = requests.post(BASE + "video/1", {"name": "my video", "likes": 10})
print(response.json())

input()

response = requests.get(BASE + "video/2")
print(response.json())