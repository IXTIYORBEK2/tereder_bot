import json
import websockets

btc_price = None


async def btc_socket():

    global btc_price

    url = "wss://stream.binance.com:9443/ws/btcusdt@trade"

    async with websockets.connect(url) as websocket:

        while True:

            data = await websocket.recv()

            data = json.loads(data)

            btc_price = data["p"]