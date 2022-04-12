import cv2
import numpy

img = cv2.imread('jawani.jpg')

img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gs.jpg', img1)

thr1 = cv2.adaptiveThreshold(
    img1, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 199, 5)
thr2 = cv2.adaptiveThreshold(
    img1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 175, 5)

cv2.imshow('original', img1)
cv2.imshow('Adaptive Mean', thr1)
cv2.imshow('Adaptive Gaussian', thr2)
cv2.waitKey(0)
