import aiohttp
from botconfig import dp, logger, OPEN_WEATHER_API_KEY
import pandas as pd
import json


def get_local_help():
    return 'Такого города нет в списке. Название города должно быть на английском.' \
           ' Команду нужно отдавать в формате /weather Moscow. '


@dp.message_handler(commands=["weather"])
async def get_openweather_response(message) -> str:
    city = message.get_args()
    df = pd.read_excel("weather/cities_list.xlsx")
    try:
        df = df.loc[df["name"] == city]
        lat = float(df["lat"])
        lon = float(df["lon"])
        try:
            url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPEN_WEATHER_API_KEY}&units=metric"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    response_text = await response.text()
                    weather_dict = json.loads(response_text)
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
        except Exception as error:
            logger.exception(error)
            weather_report = "Нет ответа от API."
    except Exception as error:
        logger.exception(error)
        weather_report = get_local_help()
    await message.answer(weather_report)
    await message.delete()


def setup(dp: dp):
    dp.register_message_handler(get_openweather_response)
