import asyncio

from app.loader import dp, bot
from app.bot.handlers.analysis import router as analysis_router
from app.bot.handlers.start import router as start_router
from app.bot.handlers.price import router as price_router
from app.bot.handlers.signals import router as signals_router
from app.scheduler.auto_signals import auto_signal_loop
from app.market.live_price import btc_socket


async def main():

    dp.include_router(start_router)
    dp.include_router(price_router)
    dp.include_router(signals_router)
    dp.include_router(analysis_router)
    asyncio.create_task(auto_signal_loop())

    asyncio.create_task(btc_socket())

    print("🔥 BOT IS RUNNING")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
   
