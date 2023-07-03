from vidgear.gears import NetGear
import serial
import cv2

cam = cv2.VideoCapture(0)

serveroptions = {"jpeg_compression": True, "jpeg_compression_quality": 95}
server = NetGear(receive_mode=False, address="172.26.45.191", port="5555", **serveroptions)

try:
    while True:
        r,f = cam.read()
        if r:
            server.send(f)
finally:
    server.close()
