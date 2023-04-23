from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

meny_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)

button_help = KeyboardButton(text="/help")
button_image = KeyboardButton(text="/image")

meny_keyboard.add(button_help, button_image)

