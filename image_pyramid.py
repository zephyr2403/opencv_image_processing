#Pyramiding image refers to either upscaling or downscaling 
import cv2 
import matplotlib.pyplot as plt 
import numpy as np 

image = cv2.imread('/home/dragonbreath/Pictures/Screenshot from 2019-01-01 22-37-03.png')

largeImage = cv2.pyrUp(image)
smallImage = cv2.pyrDown(image)

cv2.imshow('larger',largeImage)
cv2.imshow('small',smallImage)
cv2.waitKey(0)
cv2.destroyAllWindows()