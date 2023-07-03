import asyncio
from websockets.server import serve
import cv2
import numpy as np

async def recv(ws):
    async for msg in ws:
        if type(msg) == type("a"):
            print(msg)
        else:
            img = np.frombuffer(msg, dtype=np.uint8)
            img = np.reshape(img, (480,640,3))
            cv2.imshow("Camera Stream", img)
            cv2.waitKey(1)

async def main():
    async with serve(recv, "10.0.0.63", 8765):
        print("Server initialized")
        await asyncio.Future() # Receive forever

asyncio.run(main())
