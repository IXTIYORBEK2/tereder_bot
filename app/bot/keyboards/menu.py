from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton
)

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📈 BTC"),
            KeyboardButton(text="🥇 GOLD")
        ],
        [
            KeyboardButton(text="📊 Signals"),
            KeyboardButton(text="🧠 AI Analysis")
        ],
        [
            KeyboardButton(text="👤 Profile"),
            KeyboardButton(text="⚙️ Settings")
        ]
    ],
    resize_keyboard=True
)