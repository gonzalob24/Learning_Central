# Playing video from a file


import cv2
import numpy as np

video1 = cv2.VideoCapture("Dinero.mp4")  # Can't read .mov files

while(True):
    ret, frame = video1.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Frame", gray)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video1.release()
cv2.destroyAllWindows()
