import requests
from aiogram import types
from botconfig import dp, bot


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


def setup(dp: dp):
    dp.register_message_handler(send_cat_image)
