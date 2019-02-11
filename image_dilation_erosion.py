#dilation: Adds pixels to the boundaries of objects in an image 
#Erosion - removes pixels at the boundaries of object in an image 
#opening - erosion followed by dilation 
#Closing: Dilation followed by erosion 
import cv2 
import numpy as np 

image = cv2.imread('/home/dragonbreath/Pictures/Screenshot from 2019-01-01 22-37-03.png')

kernel = np.ones((5,5),np.uint8)

erosion = cv2.erode(image,kernel,iterations=1)
dilation = cv2.dilate(image,kernel,iterations=1)
cv2.imshow('Erosion',erosion)
cv2.imshow('Dilation',dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()


