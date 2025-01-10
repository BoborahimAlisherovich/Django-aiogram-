from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Savol va takliflar")],  # Each row should be a list
    ],
    resize_keyboard=True  # Ensures the keyboard adjusts its size
)
