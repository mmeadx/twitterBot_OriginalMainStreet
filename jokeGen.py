import requests

url = "https://icanhazdadjoke.com"

response = requests.get(url, headers={"Accept": "application/json"})

print(response.json()["joke"])