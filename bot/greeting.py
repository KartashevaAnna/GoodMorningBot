from aiogram import types
from config import dp, bot


HELP_COMMAND = """
<b>/help</b> - <em>список комманд</em>
<b>/start</b> - <em>начать работу с ботом</em>
"""


@dp.message_handler(commands=["help"])
async def show_all_commands(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id, text=HELP_COMMAND, parse_mode="HTML"
    )
    print(message.from_user.id)
    await message.delete()


def setup(dp: dp):
    dp.register_message_handler(show_all_commands)
