import pytest
from unittest.mock import AsyncMock
from aiogram.types import ReplyKeyboardMarkup
from tmp.simple_vote import command_start

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
