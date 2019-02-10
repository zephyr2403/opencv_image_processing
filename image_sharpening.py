#Sharpening strengtens or emphasizes on edge of the image

import cv2 
import numpy as np 


image = cv2.imread('/home/dragonbreath/Pictures/Screenshot from 2019-01-01 22-37-03.png')

#no need to normalise as sum of kernel value is one 
#if it's greator than 1 then you'll get brighter image 
# if smaller than 1 then you'll get darker image 
kernel = np.array([[-1,-1,-1],
[-1,9,-1],
[-1,-1,-1]
])
sharpened = cv2.filter2D(image,-1,kernel)

cv2.imshow('Sharpening',sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()