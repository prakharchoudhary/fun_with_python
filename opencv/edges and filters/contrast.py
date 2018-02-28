import cv2
import numpy as np

img = cv2.imread('input2.png')

img_bgr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

# equalize the histogram of the grayscale image
histeq = cv2.equalizeHist(img_bgr)

# equalize the histogram of the Y channel
img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])

# convert the YUV back to RGB image
img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

cv2.imshow('Input', img)
cv2.imshow('Input(grayscale)', img_bgr)
cv2.imshow('Histogram equalized(grayscale)', histeq)
cv2.imshow('Histogram equalized', img_output)
cv2.waitKey(0)
