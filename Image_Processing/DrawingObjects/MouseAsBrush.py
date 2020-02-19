# learn cv2.setMouseCallback()

# Create a mouse callback function which is executed when a muse event takes place.
# This event will give the coordinates (x,y) for every mouse event.

import cv2
import numpy as np

events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

drawing = False  # True if mouse is pressed
mode = True      # if Trie, draw rectangle. Press 'm to toggle to curve

ix, iy = -1, -1


# my mouse callback will draw a circle where I double click
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 100, (255, 0, 0), -1)


# This function has two modes to draw rectangles or circles
def draw_rect_or_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing is True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing is True:
            if mode is True:
                cv2.rectangle(img, (ix, iy), (x, y), (10, 255, 50), -1)
            else:
                cv2.circle(img, (x, y), 50, (5, 5, 255), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing is False
        if mode is True:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
        else:
            cv2.circle(img, (x, y), 50, (0, 0, 255), -1)


# Creates the black canvas
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('Image')
cv2.setMouseCallback('Image', draw_rect_or_circle)

while(True):
    cv2.imshow('Image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode is not mode
    elif k == ord('q'):
        break


cv2.destroyAllWindows()
