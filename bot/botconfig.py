import os
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv


load_dotenv()

TOKEN_API = os.getenv("TOKEN_API")
OPEN_WEATHER_API_KEY = os.getenv("OPENWEATHERAPIKEY")


bot = Bot(TOKEN_API)
dp = Dispatcher(bot, storage=MemoryStorage())
