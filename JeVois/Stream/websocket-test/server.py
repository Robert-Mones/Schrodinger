import asyncio
from websockets.server import serve
import time

async def recv(ws):
    async for msg in ws:
        t = time.time()
        tmsg = float(msg)
        latency = t - tmsg
        print("Received {}ms later ({}, {})".format(int(latency*1000), tmsg, t))

async def main():
    async with serve(recv, "localhost", 8765):
        print("Server initialized")
        await asyncio.Future() # Receive forever

asyncio.run(main())
