import cv2
import numpy as np

img = cv2.imread('input.jpeg')
rows, cols = img.shape[:2]

# generating vignette mask using Gaussian kernels
kernel_x = cv2.getGaussianKernel(int(1.5 * cols), 200)
kernel_y = cv2.getGaussianKernel(int(1.5 * rows), 200)

### getGaussianKernel ###
'''
-> The first parameter is to ensure the kernel is to determine its
size.

-> The second parameter is the standard deviateion of the Gaussian
and it controls the radius of the bright central region.
'''

kernel = kernel_y * kernel_x.T
mask = 255 * kernel / np.linalg.norm(kernel)
mask = mask[int(0.5 * rows):, int(0.5 * cols):]
output = np.copy(img)

# applying the mask to each channel in the input image
for i in range(3):
    output[:, :, i] = output[:, :, i] * mask

cv2.imshow('Input', img)
cv2.imshow('Vignette with shifted focus', output)

cv2.waitKey(0)
