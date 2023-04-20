import os
from aiogram import Bot, Dispatcher

from dotenv import load_dotenv


load_dotenv()

TOKEN_API = os.getenv("TOKEN_API")
OPEN_WEATHER_API_KEY = os.getenv("OPENWEATHERAPIKEY")

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
