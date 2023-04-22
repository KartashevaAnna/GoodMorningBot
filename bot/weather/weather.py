import aiohttp
from botconfig import dp, OPEN_WEATHER_API_KEY
import pandas as pd
import json


@dp.message_handler(commands=["weather"])
async def get_openweather_response(message) -> str:
    city = message.get_args()
    df = pd.read_excel("weather/cities_list.xlsx")
    df = df.loc[df["name"] == city]
    lat = float(df["lat"])
    lon = float(df["lon"])
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPEN_WEATHER_API_KEY}&units=metric"
    async with aiohttp.ClientSession() as session:
        print("first level")
        async with session.get(url) as response:
            print("second")
            response_text = await response.text()
            print(response_text)
            weather_dict = json.loads(response_text)
            print(f"response dict is {weather_dict}")
            print(f"response type dict is{type(weather_dict)} ")
            main_weather = weather_dict["weather"][0]["main"]
            description = weather_dict["weather"][0]["description"]
            temperature = weather_dict["main"]["temp"]
            feels_like = weather_dict["main"]["feels_like"]
            pressure = weather_dict["main"]["pressure"]
            humidity = weather_dict["main"]["humidity"]
            wind_speed = weather_dict["wind"]["speed"]
            weather_report = (
                f"Weather in {city} today is:\n"
                f"{main_weather}\n"
                f"{description}\n"
                f"Temperature: {temperature}\n"
                f"Feels like: {feels_like}\n"
                f"Pressure: {pressure}\n"
                f"Humidity: {humidity}\n"
                f"Wind speed: {wind_speed}"
            )
            print("weather report ", weather_report)
            await message.answer(weather_report)


def setup(dp: dp):
    dp.register_message_handler(get_openweather_response)
