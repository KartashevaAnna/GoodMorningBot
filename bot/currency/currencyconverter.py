import json


import aiohttp
from aiogram import types
from botconfig import dp, bot, CURRENCY_API_KEY


@dp.message_handler(commands=["currency"])
async def send_currency__data(message: types.Message) -> str:
    res = message.get_args()
    res = res.split(" ")
    amount = res[0]
    from_currency = res[1]
    to_currency = res[2]

    async with aiohttp.ClientSession() as session:

        def get_local_help():
            with open("currency/currencies.json", mode="r") as json_str:
                json_str = json_str.read()
                json_data = json.loads(json_str)
                local_help = f"Please, use the code of one of the currencies below: {json_data}"
                return local_help

        url = f"https://api.freecurrencyapi.com/v1/latest?apikey={CURRENCY_API_KEY}"
        try:
            async with session.get(url) as response:
                response_text = await response.text()
                rates_dict = json.loads(response_text)
                from_currency_rate_to_dollar = rates_dict["data"][from_currency]
                to_currency_rate_to_dollar = rates_dict["data"][to_currency]
                result = (
                    to_currency_rate_to_dollar / from_currency_rate_to_dollar
                ) * float(amount)
        except KeyError:
            result = get_local_help()
        await bot.send_message(message.from_user.id, text=result)


def setup(dp: dp):
    dp.register_message_handler(send_currency__data)
