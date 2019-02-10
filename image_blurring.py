# Blurring is an operation where we average the pixel with in a region(kernel)


import cv2 
import numpy as np 
import matplotlib.pyplot as plt 

image = cv2.imread('/home/dragonbreath/Pictures/Screenshot from 2019-01-01 22-37-03.png')

#7x7 kernel 
#decrease the kernel size to reduce blurring
kernel = np.ones((7,7),np.float32)/(7*7)

blurred = cv2.filter2D(image,-1,kernel)

#uses box filter 
blur = cv2.blur(image,(3,3))

#Gausian Kernel is used in gausian blur 
gblur = cv2.GaussianBlur(image,(7,7),0)

#replace the center with median in kernel value 
mblur= cv2.medianBlur(image,5)

cv2.imshow('Blurred',blurred)
cv2.imshow('Blur',blur)
cv2.imshow('GBlurred',gblur)
cv2.imshow('MBlurred',mblur)
cv2.waitKey(0)
cv2.destroyAllWindows()
