#Edge Detection
#Edge can be defined as sudden changes(discontinuities) in an image.
 
import cv2 
import numpy as np 

image = cv2.imread('/home/dragonbreath/Pictures/Screenshot from 2019-01-01 22-37-03.png')

sobel_x = cv2.Sobel(image,ddepth=-1,dx=0,dy=1,ksize=5)
sobel_y = cv2.Sobel(image,ddepth=-1,dx=1,dy=0,ksize=5)

sobel_xy = cv2.bitwise_or(sobel_x,sobel_y)
canny = cv2.Canny(image,10,100)



cv2.imshow('Image', image)
cv2.imshow('Edges in X-Direction', sobel_x)
cv2.imshow('Edges in Y-Direction', sobel_y)
cv2.imshow('Edges using sobel', sobel_xy)
cv2.imshow('Edges using Canny',canny)
cv2.waitKey(0)
cv2.destroyAllWindows()