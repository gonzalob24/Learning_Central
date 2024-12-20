# Thresholding - Binary Thresholding
# Thresholding converts grayscale image into binary

import cv2
import numpy as np

# Read the image using imread built-in function
pic = cv2.imread("Maria.jpg")
cv2.imshow("Original", pic)
cv2.waitKey(0)

# cv2.COLOR_BGR2GRAY: Converts color(RGB) image to gray
# BGR(bytes are reversed)
# cv2.cvtColor: Converts image from one color space to another
gray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)

# cv2.threshold built-in function which performs thresholding
# cv2.threshold(image, threshold_value, max_value, threshold_type)
ret, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Display threshold image using imshow built-in function
cv2.imshow("Binary Thresholding", threshold)

# Wait until any key is pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
