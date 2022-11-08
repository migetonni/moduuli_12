import requests

api_avain = "141fbef3e368ac242ac87216351df057"


kaupunki = input("Anna kaupunki ")

saa_tieto = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={kaupunki}&appid={api_avain}").json()

lat = saa_tieto["coord"]["lat"]
lon = saa_tieto["coord"]["lon"]

url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_avain}"
response = requests.get(url).json()

print(response['weather'][0]['description'], str(response['main']['temp'] - 273.15) + '°C')
