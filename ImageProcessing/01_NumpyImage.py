#pip install pillow

import numpy
from PIL import Image

arr=numpy.zeros([100,200,3],
dtype=numpy.uint8)
arr[:50,:75]=[198,40,198]
arr[:,75:]=[50,72,150]
arr[50:,:125]=[0,255,0]
arr[:25,150:190]=[0,100,200]

img=Image.fromarray(arr)
img.save('flag.png')
print('image created successfully')
