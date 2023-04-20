import os
import requests
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types

load_dotenv()
TOKEN_API = os.getenv("TOKEN_API")
OPENWEATHERAPIKEY = os.getenv("OPENWEATHERAPIKEY")

HELP_COMMAND = """
<b>/help</b> - <em>список комманд</em>
<b>/start</b> - <em>начать работу с ботом</em>
"""


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


async def on_startup(_):
    print("I have been started up")


@dp.message_handler(commands=["help"])
async def show_all_commands(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id, text=HELP_COMMAND, parse_mode="HTML"
    )
    print(message.from_user.id)
    await message.delete()


@dp.message_handler(commands=["image"])
async def send_cat_image(message: types.Message):

    random_cat_url = await get_random_cat()
    await bot.send_photo(message.from_user.id, photo=random_cat_url)
    await message.delete()


async def get_random_cat():
    URL = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(URL).json()
    random_cat_url = response[0].get("url")
    return random_cat_url

CURRENT_WEATHER_API_CALL = (
        'https://api.openweathermap.org/data/2.5/weather?'
        'lat={latitude}&lon={longitude}&'
        'appid=' + OPENWEATHERAPIKEY + '&units=metric'
)



if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
