#Segmentation: Partition Images Into Different Regions 
#Contours: Contours are continuous lines or curves that bounds or cover the full 
#boundary of an object in an image
#Contours: Continuous curves that follow the edges along a boundary
#IN OPENCV IMAGE SHOULD BE CONVERTED IN GRAYSCALE BEFORE FINDING CONTOURS
import cv2 
import numpy as np 

image = cv2.imread('/home/dragonbreath/Pictures/Screenshot from 2019-01-01 22-37-03.png')
gimage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

gimage = cv2.Canny(gimage,10,140)

# below function changes the actual image hence using image.copy()
# cv2.RETR_LIST : retrieves all contours
# cv2.RETR_EXTERNAL: retrieves external or outer contours only 
# cv2.RETR_CCOMP : retrieve all in 2-level hierarchy
# cv2.RETR_TREE : retrieves all in full hierarchy

# cv2.CHAIN_APPROX_NONE : returns all points of contours
# cv2.CHAIN_APPROX_SIMPLE: returns vertex points of contours
(_,contours,heirarchy)= cv2.findContours(gimage.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# heirarchy is stored in the following format [next,previous,first_child,parent]
print "Number Of Contours",len(contours)

#index value '-1' means last value<plot all contours>
#(0,0,255):color
#2 width
cv2.drawContours(image,contours,-1,(0,0,255),2)

cv2.imshow('Contours',image)
cv2.waitKey(0)
cv2.destroyAllWindows()