import os
import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler(f"{__name__}.log", mode='w')
formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")


load_dotenv()

TOKEN_API = os.getenv("TOKEN_API")
OPEN_WEATHER_API_KEY = os.getenv("OPENWEATHERAPIKEY")

CURRENCY_API_KEY = os.getenv("CURRENCYAPIKEY")
BASE_CURRENCY_CONVERTER_URL = (
    "https://www.google.com/search?q=convert+{}+{}+to+{}&hl=en&lr=lang_en"
)

bot = Bot(TOKEN_API)
dp = Dispatcher(bot, storage=MemoryStorage())
