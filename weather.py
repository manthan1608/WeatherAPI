import requests

API_KEY ="<Own API key>" #Enter your own API key
# BASE_URL = "http://api.openweathermap.org/geo/1.0/direct"
BASE_URL_W ="https://api.openweathermap.org/data/2.5/weather"
lat = 0
lan = 0


def getlatlon():
    global lat, lon
    BASE_URL = "http://api.openweathermap.org/geo/1.0/direct"

    limit = 5

    request_url1 = f"{BASE_URL}?q={city}&{limit}&appid={API_KEY}"
    response1 = requests.get(request_url1)

    if response1.status_code == 200:
        data = response1.json()
        # print(data[0])
        lat = data[0]['lat']
        lon = data[0]['lon']


city = input("Enter a city name: ")

limit = 5
getlatlon()
request_url2 = f"{BASE_URL_W}?lat={lat}&lon={lon}&appid={API_KEY}"
response2 = requests.get(request_url2)
if response2.status_code == 200:
    data2 = response2.json()
    # json is standardized format commonly used to transfer data as text that can be sent over a network.
    weather = data2['weather'][0]['main']
    # [0]['description'].capitalize()
    print("Weather:", weather)
    temperature = round((data2['main']['temp']-273.15),2)
    print("Temperature:", temperature, "Celsius")

else:
    print("An error occurred ")
