import requests


haku = "https://api.chucknorris.io/jokes/random"

vastaus = requests.get(haku).json()

for i in range(1):
    print(vastaus["value"])

