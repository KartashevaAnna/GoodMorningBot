import pytest
from unittest.mock import AsyncMock
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from bot.goodmorningbot import show_all_commands, HELP_COMMAND
from bot.tmp import command_start, HELP_COMMAND


# @pytest.mark.asyncio
# async def test_start_handler():
#     message = AsyncMock()
#     await show_all_commands(message)
#
#     message.reply.assert_called_with(chat_id=message.from_user.id, text=HELP_COMMAND, parse_mode="HTML")
kb = ReplyKeyboardMarkup(resize_keyboard=True)


@pytest.mark.asyncio
async def test_start_handler():
    message = AsyncMock()
    await command_start(message)

    message.reply.assert_called_with(
        chat_id=message.chat.id, text="Добро пожаловать!", reply_markup=kb
    )
