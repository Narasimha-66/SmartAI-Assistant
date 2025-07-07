import requests

API_KEY = "1938e649e70af73874f0fb5e2c5c091f"

def get_weather(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        main = data['main']
        weather_desc = data['weather'][0]['description']
        temp = main['temp']
        feels_like = main['feels_like']

        result = f"The weather in {city} is {weather_desc} with a temperature of {temp}°C, feels like {feels_like}°C."
        return result
    else:
        return f"Sorry, I couldn't find the weather for {city}."

