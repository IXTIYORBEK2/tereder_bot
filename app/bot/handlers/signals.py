from aiogram import Router
from aiogram.types import Message

from app.signals.signal_engine import analyze_btc

router = Router()


@router.message(lambda message: message.text == "📊 Signals")
async def signals_handler(message: Message):

    data = await analyze_btc()

    text = f"""
📊 BTCUSDT SIGNAL

💰 Price: {data['price']}

📈 Signal: {data['signal']}
🧠 Confidence: {data['confidence']}%

📍 Entry: {data['entry']}
🎯 TP: {data['tp']}
🛑 SL: {data['sl']}

📊 RSI: {data['rsi']}
"""

    await message.answer(text)