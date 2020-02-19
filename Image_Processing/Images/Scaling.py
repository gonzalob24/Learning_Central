# Scaling  is simpling resizing an image -- cubic, area, linear interpolations
# Interpolation is a method of estimating values between data points.

import cv2
import numpy as np

# Do the same to read and show the original picture
pic = cv2.imread("Maria.jpg")
cv2.imshow("Original", pic)

cv2.waitKey(0)

# cv2.resize(image, output image size, x scale, y scale, interpolation)

# Scaling using cubic interpolation
scaling_cubic = cv2.resize(pic, None, fx=.50, fy=.50, interpolation=cv2.INTER_CUBIC)
cv2.imshow("Cubic Interpolation", scaling_cubic)
cv2.waitKey(0)


# Scaling using area interpolation.The image will look skewed
scaling_area = cv2.resize(pic, (600, 300), interpolation=cv2.INTER_AREA)
cv2.imshow("Area Interpolation", scaling_area)
cv2.waitKey(0)


# Scaling using linear interpolation
scaling_linear = cv2.resize(pic, None, fx=.50, fy=.5, interpolation=cv2.INTER_LINEAR)
cv2.imshow("Linear Interpolation", scaling_linear)
cv2.waitKey(0)

cv2.destroyAllWindows()
