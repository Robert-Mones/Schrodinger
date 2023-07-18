import multiprocessing as mp
import asyncio
from websockets.server import serve

client_queue = None
client_proc = None

# Function which starts a process for runClient and returns immediately
def launchClient(ip_client, port_serial):
    global client_queue, client_proc
    client_queue = mp.Queue()
    client_proc = mp.Process(target=runClient, args=(ip_client, port_serial, client_queue))
    client_proc.start()

# Function which instructs the client to quit
def closeClient():
    global client_queue, client_proc
    if client_queue == None or client_proc == None:
        print("No client to close")
        return
    # Placing anything in the client_queue will instruct the client to close
    client_queue.put(0)
    client_proc.join()

async def recv(ws):
    async for msg in ws:
        print(msg)

async def waitForQueue(client_queue):
    while client_queue.empty():
        await asyncio.sleep(0.1)

async def main(ip_client, port_serial, client_queue):
    async with serve(recv, ip_client, port_serial):
        await waitForQueue(client_queue)

# Function which runs the serial client but does not return
def runClient(ip_client, port_serial, client_queue):
    asyncio.run(main(ip_client, port_serial, client_queue))
