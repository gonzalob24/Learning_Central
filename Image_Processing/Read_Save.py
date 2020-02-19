import cv2
import numpy as np


# cv2.imread() loads the image
bird_pic = cv2.imread("bird.jpg")
cv2.imshow("bird_pic", bird_pic)
# cv2.imshow(image_name, flag how image should be read)shows the image
# flag can be:
#       cv2.IMREAD_COLOR or 1
#       cv2.IMREAD_GRAYSCALE or 0
#       cv2.IMREAD_UNCHANGED or - 1 or leave blank

#  This allows to resize the window
# cv2.WINDOW_NORMAL allows to resize
# cv2.namedWindow("bird_pic", cv2.WINDOW_NORMAL)
k = cv2.waitKey(0)  # Keyboard binding function, time is in milliseconds

if k == 10:  # Wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord("s"):  # S key is to save image
    cv2.imwrite("bird_pic_gray.jpg", bird_pic)
    cv2.destroyAllWindows()


# cv2.imshow("bird_pic", bird_pic)

# cv2.imwrite("bird_pic_gray.jpg", bird_pic)

# Waite till user presses enter
# cv2.waitKey()  # Keyboard binding function, time is in milliseconds
# cv2.destroyAllWindows()  # Can pass the name of window you want to kill

