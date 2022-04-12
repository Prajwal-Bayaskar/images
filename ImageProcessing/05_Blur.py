import cv2

img=cv2.imread('jawani.jpg')
cv2.imshow('Original image',img)
cv2.waitKey(0)

#Gaussian blur
gs=cv2.GaussianBlur(img,(7,7),0)
cv2.imshow('Gaussian Blur',gs)
cv2.waitKey(0)

#Median blurr
md=cv2.medianBlur(img,9)
cv2.imshow('Median Blur',md)
cv2.waitKey(0)

#Bilateral blur
bl=cv2.bilateralFilter(img,25,75,75)
cv2.imshow('Bilateral blur',bl)
cv2.waitKey(0)

cv2.destroyAllWindows()