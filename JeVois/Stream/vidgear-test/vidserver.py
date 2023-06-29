from vidgear.gears import NetGear
import cv2

cam = cv2.VideoCapture(0)
server = NetGear(receive_mode=False, address="10.0.0.63", port="5555")

try:
    while True:
        r,f = cam.read()
        if r:
            server.send(f)
finally:
    server.close()
