import cv2

cam = cv2.VideoCapture(0)

while True:
    r,frame = cam.read()

    if r:
        cv2.imshow("Camera", frame)
        cv2.waitKey(1)
    else:
        print("Failed to read")