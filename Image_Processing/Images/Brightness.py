# varying the brightness if an image using add and subtract

import cv2
import numpy as np

# Read the image the same way as before
pic = cv2.imread("Maria.jpg")
cv2.imshow("Original", pic)
cv2.waitKey(0)

# np.ones returns an array of given shape and type, filled with ones
# np.ones(shape, dtype)

matrix = np.ones(pic.shape, dtype="uint8") * 120
# image.shape: gives takes the shape of original image
# uint8: unsigned integer (0 to 255)
# matrix: contains ones, having same dimension as original image but mutlipied by 120

# Adding matrix to original image, increases brightness
add = cv2.add(pic, matrix)
cv2.imshow("Added", add)
cv2.waitKey(0)

# Subtract matrix from original image decreases the brightness
subtract = cv2.subtract(pic, matrix)
cv2.imshow("Subtracted", subtract)
cv2.waitKey(0)

cv2.destroyAllWindows()
