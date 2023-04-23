import json


import aiohttp
from aiogram import types
from botconfig import dp, bot, logger, CURRENCY_API_KEY


def get_local_help() -> str:
    with open("currency/currencies.json", mode="r") as json_str:
        json_str = json_str.read()
        json_data = json.loads(json_str)
        local_help = f"Please, use the code of one of the currencies below: {json_data}"
        return local_help


@dp.message_handler(commands=["convert"])
async def send_currency__data(message: types.Message) -> str:
    user_inputs = message.get_args()
    inputs_list = user_inputs.split(" ")
    try:
        amount = float(inputs_list[0])
        from_currency = inputs_list[1]
        to_currency = inputs_list[2]

        async with aiohttp.ClientSession() as session:
            try:
                url = f"https://api.freecurrencyapi.com/v1/latest?apikey={CURRENCY_API_KEY}"
                try:
                    async with session.get(url) as response:
                        response_text = await response.text()
                        rates_dict = json.loads(response_text)
                        if from_currency == "USD" or to_currency == "USD":
                            if from_currency != "USD":
                                from_currency_rate_to_dollar = rates_dict["data"][from_currency]
                                result = from_currency_rate_to_dollar * amount
                            else:
                                to_currency_rate_to_dollar = rates_dict["data"][to_currency]
                                result = to_currency_rate_to_dollar / amount
                        else:
                            from_currency_rate_to_dollar = rates_dict["data"][from_currency]
                            to_currency_rate_to_dollar = rates_dict["data"][to_currency]
                            result = (
                                             to_currency_rate_to_dollar / from_currency_rate_to_dollar
                                     ) * float(amount)
                except KeyError:
                    logger.exception(KeyError)
                    result = get_local_help()
            except Exception as error:
                logger.exception(error)
                result = 'Нет ответа от API.'
    except Exception as error:
        logger.exception(error)
        result = get_local_help()
    await bot.send_message(message.from_user.id, text=result)
    await message.delete()


def setup(dp: dp):
    dp.register_message_handler(send_currency__data)
