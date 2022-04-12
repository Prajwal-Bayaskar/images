import numpy
import cv2

img = cv2.imread('jawani.jpg')
x = numpy.ones((5, 5), numpy.uint8)

ero=cv2.erode(img, x, iterations = 1)
dil=cv2.dilate(img, x, iterations = 1)

cv2.imshow("Original", img)
cv2.imshow("Erosion", ero)
cv2.imshow("Dilation", dil)

cv2.waitKey(0)
