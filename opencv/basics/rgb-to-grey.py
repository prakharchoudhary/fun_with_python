import cv2

image = cv2.imread(raw_input("Enter the path of the image file: "),
                   cv2.IMREAD_GRAYSCALE)

cv2.imwrite('Testpic.png', image)	
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()