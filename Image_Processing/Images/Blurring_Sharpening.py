# Blurring and Sharpening Images

import cv2
import numpy as np

# Read and show original
pic = cv2.imread("Maria.jpg")
cv2.imshow("Original", pic)
cv2.waitKey(0)

# Blurring images: Averaging, cv2.blur built-in function
# Averaging: Convolving image with normalized box filter

# Convolution: Mathematical operation on 2 functions which produces third function.
# Normalized box filter having size 3 x 3 would be:
# (1/9)  [[1, 1, 1],
#		 [1, 1, 1],
# 		 [1, 1, 1]]
blur = cv2.blur(pic,(9,9)) # (9 x 9) filter is used

# Display blurred image
cv2.imshow('Blurred', blur)
cv2.waitKey(0)

# Sharpening images: Emphasizes edges in an image

kernel = np.array([[-1,-1,-1],
                   [-1,9,-1],
                   [-1,-1,-1]])

# If we don't normalize to 1, image would be brighter or darker respectively

# cv2.filter2D is the built-in function used for sharpening images
# cv2.filter2D(image, ddepth, kernel)
sharpened = cv2.filter2D(pic, -1, kernel)
# ddepth = -1, sharpened images will have same depth as original image

# Display sharpenend image
cv2.imshow('Sharpened', sharpened)
cv2.waitKey(0)

cv2.destroyAllWindows()
