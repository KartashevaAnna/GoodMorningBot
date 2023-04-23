from aiogram import types


from botconfig import dp, bot
from keyboards.keyboards import meny_keyboard


HELP_COMMAND = """
<b>/help</b> - <em>Cписок команд</em>
<b>/start</b> - <em>Вызвать основное меню</em>
<b>/image</b> - <em>Получить изображение котика</em>
<b>/weather</b> - <em>Узнать погоду.</em> Пример: <b>Weather Moscow</b>
<b>/convert</b> - <em>Конвертировать валюту.</em> Пример: <b>/convert 100 RUB EUR</b>
"""


@dp.message_handler(commands=["help"])
async def show_all_commands(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id, text=HELP_COMMAND, parse_mode="HTML"
    )
    print(message.from_user.id)
    await message.delete()


@dp.message_handler(commands=["start"])
async def start_button(message: types.Message):
    await message.answer(
        text="Добро пожаловать в основное меню! 🐝",
        reply_markup=meny_keyboard,
    )
    await message.delete()


def setup(dp: dp):
    dp.register_message_handler(show_all_commands)
    dp.register_message_handler(start_button)
