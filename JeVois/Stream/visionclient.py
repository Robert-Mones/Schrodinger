from websockets.sync.client import connect
import vidclient
import serclient
import psutil

ip_client = psutil.net_if_addrs()["wlp0s20f3"][0].address
ip_server = "rmones-schzero.wifi.local.cmu.edu"
port_inf = 8001
port_video = 8101
port_serial = 8102

def runClient():
    # Connect to the server via the infrastructure port (8001) and sends a
    # stream request for video and serial data
    with connect("ws://{}:{}".format(ip_server, port_inf)) as ws:
        ws.send("stream_request,{},{},{}".format(ip_client, port_video, port_serial))
    
    # Open video stream
    vidclient.launchClient(ip_client, port_video)
    # Open serial stream
    serclient.launchClient(ip_client, port_serial)

if __name__ == "__main__":
    runClient()
