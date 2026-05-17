import asyncio

from app.loader import bot
from app.signals.signal_engine import analyze_btc



CHAT_ID='1152187206'


async def auto_signal_loop():

    while True:

        data = await analyze_btc()

        if data["signal"] != "NEUTRAL":

            text = f"""
🚨 AUTO SIGNAL

📈 {data['signal']}

💰 Price: {data['price']}

🎯 TP: {data['tp']}
🛑 SL: {data['sl']}

🧠 Confidence: {data['confidence']}%
"""

            await bot.send_message(CHAT_ID, text)

        await asyncio.sleep(300)