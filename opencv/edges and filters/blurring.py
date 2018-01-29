import cv2
import numpy as np

img = cv2.imread('input.jpeg')
rows, cols = img.shape[:2]

kernel_identity = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
kernel_3x3 = np.ones((3, 3), np.float32) / 9.0
kernel_5x5 = np.ones((5, 5), np.float32) / 25.0

cv2.imshow('Original', img)

output = cv2.filter2D(img, -1, kernel_identity)
cv2.imshow('Identity filter', output)

output = cv2.filter2D(img, -1, kernel_3x3)
cv2.imshow('3x3 filter', output)

output = cv2.filter2D(img, -1, kernel_5x5)
cv2.imshow('5x5 filter', output)

### Using OpenCV function ###
# output = cv2.blur(img, (3,3))   # for a 3x3 kernel
# cv2.imshow('3x3 filter(using blur func)', output)

cv2.waitKey(0)
cv2.destroyAllWindows()
