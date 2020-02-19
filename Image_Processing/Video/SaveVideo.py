# VideoWriter object specify output file name and FourCC Code and fps
# FourCC is a 4-byte code for video codec
# Also specify color with isColor flag

# FoursCC passed as
# cv2.VideoWriter_fourcc("M", "J", "P", "G") or
# cv2.VideoWriter_fourcc(*'MJPG)

# Codecs we hav
# DIVX, XVID, MJPG, X264, WMVI, WMV2

# Below code capture video from a camera, flip evry frame in vertical direction
# and save it

import cv2
import numpy as np

video = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# output object
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while(video.isOpened()):
    ret, frame = video.read()

    if ret is True:
        frame = cv2.flip(frame, 0)

        # write the flipped frame
        out.write(frame)
        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
video.release()
out.release()
cv2.destroyAllWindows()
