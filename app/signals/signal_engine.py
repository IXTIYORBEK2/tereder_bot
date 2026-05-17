from app.market.candles import get_btc_candles
from app.indicators.rsi import calculate_rsi


async def analyze_btc():

    closes = await get_btc_candles()

    current_price = closes[-1]

    rsi = calculate_rsi(closes)

    signal = "NEUTRAL"
    confidence = 50

    if rsi < 30:
        signal = "BUY"
        confidence = 82

    elif rsi > 70:
        signal = "SELL"
        confidence = 84

    entry = round(current_price, 2)

    tp = round(entry * 1.01, 2)

    sl = round(entry * 0.995, 2)

    return {
        "price": current_price,
        "rsi": rsi,
        "signal": signal,
        "confidence": confidence,
        "entry": entry,
        "tp": tp,
        "sl": sl
    }