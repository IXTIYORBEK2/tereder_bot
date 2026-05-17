from aiogram import Router
from aiogram.types import Message

from app.signals.signal_engine import analyze_btc
from app.ai.market_analysis import generate_analysis

router = Router()


@router.message(lambda message: message.text == "🧠 AI Analysis")
async def ai_analysis_handler(message: Message):

    signal_data = await analyze_btc()

    analysis = await generate_analysis(signal_data)

    await message.answer(analysis)