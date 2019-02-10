#Image Arithematic can be utilised to increase or decrease brightness 

import cv2 
import matplotlib.pyplot as plt 
import numpy as np 

image = cv2.imread('/home/dragonbreath/Pictures/Screenshot from 2019-01-01 22-37-03.png')

#creating matrix of dimension image.shape 
#changing 75 will increase of decrease the level of brightness
matOnes = np.ones(image.shape,dtype='uint8') * 75 

#adding created matrix containing 75 to the image 
increaseBrightness = cv2.add(image,matOnes)
decreseBrightness = cv2.subtract(image,matOnes)

cv2.imshow('IB',increaseBrightness)
cv2.imshow('DB',decreseBrightness)
cv2.waitKey(0)
cv2.destroyAllWindows()