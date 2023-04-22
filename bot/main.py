from botconfig import dp
from aiogram import executor


import cute_image
import help
from weather import weather
from currency import currencyconverter


async def on_startup(_):
    print("I have been started up")


if __name__ == "__main__":
    help.setup(dp)
    weather.setup(dp)
    currencyconverter.setup(dp)
    cute_image.setup(dp)
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
