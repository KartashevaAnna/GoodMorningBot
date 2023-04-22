import os
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv


load_dotenv()

TOKEN_API = os.getenv("TOKEN_API")
OPEN_WEATHER_API_KEY = os.getenv("OPENWEATHERAPIKEY")

CURRENCY_API_KEY = os.getenv("CURRENCYAPIKEY")
BASE_CURRENCY_CONVERTER_URL = (
    "https://www.google.com/search?q=convert+{}+{}+to+{}&hl=en&lr=lang_en"
)

bot = Bot(TOKEN_API)
dp = Dispatcher(bot, storage=MemoryStorage())
