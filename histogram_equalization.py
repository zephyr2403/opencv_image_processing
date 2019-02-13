#Equalize the distribution of histogram to increase contrast

#STEPS:
'''
Convert image into HSV
Select the value channel from HSV
Apply the HistogramEqualization of Value Channel
'''

def plot_hist(image,title):
    color = ('b','g','r')
    for i,c in enumerate(color):
        hist = cv2.calcHist([image],[i],None,[256],[0,256])
        plt.plot(hist,color=c)
    plt.title(title)
    plt.show()

import cv2
import matplotlib.pyplot as plt 
import numpy as np 

image = cv2.imread('/home/dragonbreath/Pictures/r3.png')
cv2.imshow('N',image)
plot_hist(image,'Before Hist Equalization')

hsv_img = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

hsv_img[:,:,2] = cv2.equalizeHist(hsv_img[:,:,2])

image = cv2.cvtColor(hsv_img,cv2.COLOR_HSV2BGR)
plot_hist(image,'After Hist Equalization')
cv2.imshow('HN',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
