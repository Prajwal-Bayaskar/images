# pip install OpenCV-python
import cv2

filenm = 'jawani.jpg'

try:
    img = cv2.imread(filenm)
    width, height = img.shape[:2]
    res = cv2.resize(img, (int(width/4), int(height/4)),
                     interpolation=cv2.INTER_CUBIC)
    cv2.imwrite('toosmall.jpg', res)
    print('image size changed and saved')
except:
    print('cant resize')
