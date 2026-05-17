from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from app.bot.keyboards.menu import main_menu

router = Router()

@router.message(CommandStart())
async def start_cmd(message: Message):

    text = """
🔥 Welcome to Premium Trading Bot

📈 Live Market
🧠 AI Analysis
📊 Smart Signals
⚡ Real-time Alerts
"""

    await message.answer(
        text,
        reply_markup=main_menu
    )