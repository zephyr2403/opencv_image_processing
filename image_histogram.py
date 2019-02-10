import cv2 
import numpy as np 
import matplotlib.pyplot as plt 

image = cv2.imread(r'/home/dragonbreath/Pictures/gg.png')

histb = cv2.calcHist(image,
                        [0], #histogram for blue color
                        None, #mask
                        [256], #histogram size 
                        [0,256] #histogram range
                        )
histg = cv2.calcHist(image,
                        [1], #histogram for green color
                        None,
                        [256],
                        [0,256]
                        )
histr = cv2.calcHist(image,
                        [2], #histogram for red color
                        None,
                        [256],
                        [0,256]
                        )

plt.plot(histb,color='blue')
plt.plot(histg,color='green')
plt.plot(histr,color='red')
plt.show()