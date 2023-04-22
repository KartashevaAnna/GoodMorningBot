from aiogram import types


from botconfig import dp, bot
from keyboards.keyboards import meny_keyboard


HELP_COMMAND = """
<b>/help</b> - <em>список комманд</em>
<b>/start</b> - <em>начать работу с ботом</em>
<b>/image</b> - <em>получить изображение котика</em>
<b>/weather</b> - <em>узнать погоду</em>
<b>/vote</b> - <em>проголосать  за фото </em>

Чтобы вызвать клавиатуру с командами, наберите <b>/start</b>.

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
