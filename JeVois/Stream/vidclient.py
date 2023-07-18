from vidgear.gears import NetGear
import multiprocessing as mp
import cv2

client_queue = None
client_proc = None

# Function which starts a process for runClient and returns immediately
def launchClient(ip_client, port_video):
    global client_queue, client_proc
    client_queue = mp.Queue()
    client_proc = mp.Process(target=runClient, args=(ip_client, port_video, client_queue))
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

# Function which runs the video client but does not return
def runClient(ip_client, port_video, client_queue):
    options = {}
    client = NetGear(receive_mode=True, address=ip_client, port=port_video, **options)

    try:
        while client_queue.empty():
            frame = client.recv()
            if frame is None:
                break
            cv2.imshow("Video Stream", frame)
            cv2.waitKey(1)
    finally:
        cv2.destroyAllWindows()
        client.close()
