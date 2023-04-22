from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

meny_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)

button_help = KeyboardButton(text="/help")
button_image = KeyboardButton(text="/image")
button_weather = KeyboardButton(text="/weather")

meny_keyboard.add(button_help)
meny_keyboard.add(button_image, button_weather)
