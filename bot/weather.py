import aiohttp
from aiogram import types
from config import dp, OPEN_WEATHER_API_KEY


CURRENT_WEATHER_API_CALL = (
    "https://api.openweathermap.org/data/2.5/weather?"
    "lat={latitude}&lon={longitude}&"
    "appid=" + OPEN_WEATHER_API_KEY + "&units=metric"
)


def get_keyboard():
    keyboard = types.ReplyKeyboardMarkup()
    button = types.KeyboardButton("Share Position", request_location=True)
    keyboard.add(button)
    return keyboard


@dp.message_handler(content_types=["location"])
async def handle_location(message: types.Message):
    latitude = message.location.latitude
    longitude = message.location.longitude
    reply = "latitude:  {}\nlongitude: {}".format(latitude, longitude)
    print(
        latitude,
        longitude,
    )
    await message.answer(reply, reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(commands=["locate_me"])
async def cmd_locate_me(message: types.Message):
    reply = "Click on the the button below to share your location"
    await message.answer(reply, reply_markup=get_keyboard())


@dp.message_handler(commands=["weather"])
async def _get_openweather_response(latitude: float, longitude: float) -> str:
    url = CURRENT_WEATHER_API_CALL.format(latitude=latitude, longitude=longitude)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response_text = await response.text()
            print(f"here is my response {response_text}")
            return response_text


def setup(dp: dp):
    dp.register_message_handler(get_keyboard)
    dp.register_message_handler(handle_location)
    dp.register_message_handler(cmd_locate_me)
    dp.register_message_handler(_get_openweather_response)
