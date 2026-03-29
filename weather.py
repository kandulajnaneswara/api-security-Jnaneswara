import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

if API_KEY is None:
    raise ValueError("API KEY not found. Please set it in the .env file.")

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    try:
        response = requests.get(url)

        if response.status_code == 429:
            print("Error: Too many requests. Please wait and try again later.")
            return
        elif response.status_code != 200:
            print(f"Error: Failed to fetch data. Status Code: {response.status_code}")
            return
        
        data = response.json()

        temperature = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]

        print(f"Temperature: {temperature}")
        print(f"Weather: {weather_desc}")
    
    except requests.exceptions.RequestException as e:
        print("Error: Network issue or API Request failed. ")
        print(e)

city = input("Enter City Name: ")


get_weather(city)