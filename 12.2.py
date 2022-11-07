import requests
import json

paikkakunta_nimi = input("Anna paikkakunta")

kaupunki_muutin = "http://api.openweathermap.org/geo/1.0/direct?q=" + paikkakunta_nimi + "141fbef3e368ac242ac87216351df057"

vastaus1 = requests.get(kaupunki_muutin).json()

print(vastaus1)

saa_haku = "https://api.openweathermap.org/data/3.0/onecall?lat=" + vastaus1 + "141fbef3e368ac242ac87216351df057"

print(json.dumps(saa_haku, indent=2))