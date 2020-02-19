# Edge Detection using Canny edge detector
# Edges are set of points(lines), where image brightness changes sharply

import cv2

# Read the image using imread built-in function
pic = cv2.imread('Maria.jpg')
cv2.imshow("Original", pic)
cv2.waitKey(0)

# cv2.Canny is the built-in function used to detect edges
# cv2.Canny(image, threshold_1, threshold_2)
canny = cv2.Canny(pic, 50, 200)

# Display edge detected output image using imshow built-in function
cv2.imshow('Canny Edge Detection', canny)

# Wait until any key is pressed
cv2.waitKey(0)

cv2.destroyAllWindows()
