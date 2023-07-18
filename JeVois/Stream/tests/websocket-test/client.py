from websockets.sync.client import connect
import time

def ping(n):
    with connect("ws://localhost:8765") as ws:
        for i in range(n):
            time.sleep(1)
            t = time.time()
            ws.send(str(t))

ping(10)
