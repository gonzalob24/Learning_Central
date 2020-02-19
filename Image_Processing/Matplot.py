import cv2
import numpy as np
from matplotlib import pyplot as plt
# import matplotlib.pyplot as plt

# Note OpenCV is in BGR mode and Matplotlib is in RGB mode
# Look at mot plot 2 for fixture
bird = cv2.imread("bird.jpg")
plt.imshow(bird, cmap = 'gray', interpolation = "bicubic")
plt.xticks([]), plt.yticks([])  # To hide tick values on x and y axis
cv2.cvtColor(bird, cv2.COLOR_BGR2RGB)
plt.show()
