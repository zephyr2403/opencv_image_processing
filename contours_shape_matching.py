import cv2
import numpy as np 

img = image = cv2.imread('/home/dragonbreath/Pictures/tt.png',0)
target_imagergb = cv2.imread('/home/dragonbreath/Pictures/Screenshot from 2019-01-01 22-37-03.png')

target_image = cv2.cvtColor(target_imagergb,cv2.COLOR_BGR2GRAY)
cv2.imshow('Imagew',target_imagergb)
_,img_thres = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
_,target_thres = cv2.threshold(target_image,127,255,cv2.THRESH_BINARY)

_,img_contours,_ = cv2.findContours(img_thres,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
_,target_contours,_ = cv2.findContours(target_thres,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

img_contours = img_contours[2]
prevmatch=200
for contour in target_contours:
    #Lower the match closer the image
    match = cv2.matchShapes(img_contours,contour,1,0.0)
    #print match 
    if prevmatch > match and match !=0.0:
        matchingContours = contour
        prevmatch = match 
        
print prevmatch
cv2.drawContours(target_imagergb,[matchingContours],-1,(0,0,255),5)
cv2.imshow('Imagze',img)

cv2.imshow('Image',target_imagergb)
# cv2.imshow('rs',img_thres)
cv2.waitKey(0)
cv2.destroyAllWindows()