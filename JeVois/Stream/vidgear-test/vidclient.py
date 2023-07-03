from vidgear.gears import NetGear
import cv2

options = {}
client = NetGear(receive_mode=True, address="172.26.45.191", port="5555", **options)

try:
    while True:
        frame = client.recv()
        if frame is None:
            break

        cv2.imshow("Video Stream", frame)
        cv2.waitKey(1)
finally:
    cv2.destroyAllWindows()
    client.close()
