async def generate_analysis(signal_data):

    signal = signal_data["signal"]
    rsi = signal_data["rsi"]

    text = ""

    if signal == "BUY":

        text = f"""
🧠 AI ANALYSIS

Market looks bullish.

RSI is currently at {rsi},
which indicates oversold conditions.

Possible upward movement expected.
"""

    elif signal == "SELL":

        text = f"""
🧠 AI ANALYSIS

Market looks bearish.

RSI is currently at {rsi},
which indicates overbought conditions.

Possible downward movement expected.
"""

    else:

        text = f"""
🧠 AI ANALYSIS

Market is neutral.

RSI: {rsi}

No strong confirmation yet.
"""

    return text