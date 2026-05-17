import aiohttp


async def get_btc_candles():

    url = (
        "https://api.binance.com/api/v3/klines"
        "?symbol=BTCUSDT&interval=1m&limit=100"
    )

    async with aiohttp.ClientSession() as session:

        async with session.get(url) as response:

            data = await response.json()

            closes = []

            for candle in data:
                closes.append(float(candle[4]))

            return closes