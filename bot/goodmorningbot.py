from config import dp
from aiogram import executor


import cute_image
import greeting
import weather


async def on_startup(_):
    print("I have been started up")


if __name__ == "__main__":
    greeting.setup(dp)
    weather.setup(dp)
    cute_image.setup(dp)
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
