# cv2.line() cv2.circle() cv2.rectangle() cv2.ellipse() cv2.putText()

# img: image where i want to draw the shapes
# color: color fo shape for BGR use tuple (255, 0, 0) for blue
# thickness: -1 for closed figures will fill shape, default = 1
# lineType: cv2.LINE_...

# Drawing a line

import cv2
import numpy as np

#Create a black image

img = np.zeros((512, 512, 3), np.uint8) # Creates a black window


# Draw a diagonal blue line with thickness 5 px
img = cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

# Drawing rectangle
img = cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

# Drawing Circle
img = cv2.circle(img, (447, 63), 50, (0, 0, 255), 20)

# Drawing an Ellipse
img = cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)

# Draw Polygon
# First I need coordinates of vertices.  Make pts into an array
# of shape ROWSx1x2 rows are number of vertices with int 32
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
img = cv2.polylines(img, [pts], True, (0, 255, 255))

# Adding text to images
# Data starts at bottom left corner
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV is cool!', (10, 500), font, 4, (255, 255, 255), 2, cv2.LINE_AA)
cv2.imshow('Blue Line', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
