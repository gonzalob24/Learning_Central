# Flipping an image -- Horizontally, Vertically, Horizontally & Vertically

import cv2

# Read and show the image the same way as before
pic = cv2.imread('Maria.jpg')
cv2.imshow("Original", pic)
cv2.waitKey(0)

# Horizontal flip
horizontal_flip = cv2.flip(pic, 1)
cv2.imshow("Horizontal Flip", horizontal_flip)
cv2.waitKey(0)

# Vertical flip
vertical_flip = cv2.flip(pic, 0)
cv2.imshow("Vertical Flip", vertical_flip)
cv2.waitKey(0)

# Horizontal and vertica
h_v_flipping = cv2.flip(pic, -1)
cv2.imshow("Horizontal and Vertical Flipping", h_v_flipping)
cv2.waitKey(0)

cv2.destroyAllWindows()
