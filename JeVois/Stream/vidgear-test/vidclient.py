from vidgear.gears import NetGear
import cv2

client = NetGear(receive_mode=True, address="10.0.0.63", port="5555")

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