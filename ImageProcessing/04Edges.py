import cv2

img=cv2.imread('jawani.jpg')
edges=cv2.Canny(img,100,200)
cv2.imwrite('lines.jpg',edges)
print('image converted with edge detection')