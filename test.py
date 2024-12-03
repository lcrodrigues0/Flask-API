import requests

BASE = "http://127.0.0.1:5000/"

data = [
    {"name": "video 1", "likes": 10, "views": 10000},
    {"name": "video 2", "likes": 20, "views": 10000},
    {"name": "video 3", "likes": 30, "views": 10000},
]

for i in range(len(data)):
    response = requests.post(BASE + "video/" + str(i), data[i])
    print(response.json())

input()

response = requests.delete(BASE + "video/0")
print(response)

input()

response = requests.get(BASE + "video/2")
print(response.json())