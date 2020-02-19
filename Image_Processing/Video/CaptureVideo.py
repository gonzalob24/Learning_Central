# read video, display video and save video
# cv2.VideoCapture()
# cv2VideoWrite()

import cv2
import numpy as np

# live stream using built in webcam and convert to gray scale

stream1 = cv2.VideoCapture(0)  # VideoCapture object pass 0 or -1 or 1 depending on the cameras connected

while(True):
    # Capture frame by frame
    # ret, frame = stream1.read()
    # read() returns boolean operation
    # If frame is read correctly  it will return True

    if stream1.isOpened():
        ret, frame = stream1.read()

        # My operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # stream1.set(propId=3, value=2)
        # stream1.get(3)
        # ret = stream1.set(4, 240)

        # Display the resulting frame
        cv2.imshow("Frame", gray)

    if cv2.waitKey(1) & 0xFF == ord("q"):  # & is for bit wise operation
        break

# When everything is done release the capture
stream1.release()
cv2.destroyAllWindows()
