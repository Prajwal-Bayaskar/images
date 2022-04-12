import cv2

img=cv2.imread('jawani.jpg')
(rows,cols)=img.shape[:2]

i=cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
res=cv2.warpAffine(img,i,(cols,rows))
cv2.imwrite('rotate.jpg',res)
print('image roatated and saved')