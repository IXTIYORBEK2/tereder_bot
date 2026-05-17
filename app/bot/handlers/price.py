from aiogram import Router
from aiogram.types import Message

from app.market.live_price import btc_price

router = Router()

@router.message(lambda message: message.text == "📈 BTC")
async def btc_handler(message: Message):

    if btc_price is None:
        await message.answer("⏳ Loading live market...")
        return

    text = f"""
₿ BTCUSDT LIVE

💰 Price: {btc_price}
⚡ Source: Binance WebSocket
"""

    await message.answer(text)