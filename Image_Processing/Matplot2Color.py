import cv2
import numpy as np
import matplotlib.pyplot as plt

bird = cv2.imread("bird.jpg")
b, g, r = cv2.split(bird)

bird2 = cv2.merge([r, g, b])

plt.subplot(121);plt.imshow(bird)
plt.subplot(121);plt.imshow(bird2)
plt.show()

cv2.imshow("BGR Image", bird)
cv2.imshow("RGB Image", bird2)

cv2.waitKey()
cv2.destroyAllWindows()
