#Thresholding is act of converting an image to a binary form
#IMAGES NEED TO BE CONVERTED INTO GREY SCALE BEFORE THRESHOLDING 

import cv2 
import numpy as np 

image = cv2.imread('/home/dragonbreath/Pictures/Screenshot from 2019-01-01 22-37-03.png',0) #0 => convert to grayscale

#below 120 goes to 0, above 120 goes to 255 
_,tBinary = cv2.threshold(image,120,255,cv2.THRESH_BINARY)

#below 120 goes to 255, above 120 goes to 0 
_,tBinaryInv = cv2.threshold(image,120,255,cv2.THRESH_BINARY_INV)

#values above 120 are 120
_,thresTruc = cv2.threshold(image,120,255,cv2.THRESH_TRUNC)

#values below 120 goes to 0, above 120 are unchanged
_,thresTozero =  cv2.threshold(image,120,255,cv2.THRESH_TOZERO)

#values below 120 unchanged, above 127 goes to 0  
_,thresTozeroInv = cv2.threshold(image,120,255,cv2.THRESH_TOZERO_INV)

cv2.imshow('THRESH_BINARY',tBinary )
cv2.imshow('THRESH_BINARY_INV',tBinaryInv)
cv2.imshow('THRESH_TRUNC',thresTruc)
cv2.imshow('THRESH_TOZERO',thresTozero)
cv2.imshow('THRESH_TOZERO_INV',thresTozeroInv)
cv2.waitKey(0)
cv2.destroyAllWindows()