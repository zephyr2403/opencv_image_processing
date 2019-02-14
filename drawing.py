import cv2
import numpy as np 

def display(img):
    cv2.namedWindow('Edits',cv2.WINDOW_AUTOSIZE)
    cv2.imshow('Edits',img)
    cv2.waitKey(0)

def drawLine(img):
    cv2.line(img,(20,20),(20,200),(255,0,0),thickness=2,lineType=cv2.LINE_AA)


def drawCircle(img):
              #img    #center    #radius   #color 
    cv2.circle(img,  (150,150)   ,20,     (0,0,255),    thickness=2,lineType=cv2.LINE_8)


def drawEllipse(img):
             #image   #center     #x y radius  #rotation <  #starting <     #ending <    #rgb
    cv2.ellipse(img,  (150,150),  (100,50),    90,            0,             360        ,(255,0,0),thickness=4,lineType=cv2.LINE_AA)


def drawRectangle(img):
    cv2.rectangle(img,(0,0),(200,200),(0,255,0),thickness=1,lineType=cv2.LINE_4)


def writeImg(img):
    cv2.putText(img,'Dishonored',(60,280),cv2.FONT_HERSHEY_DUPLEX,1,(255,0,100),2)


def main():
    img = cv2.imread(r'/home/dragonbreath/Pictures/tt.png',1)
    if img is None:
        print "Error"
    else:
        drawLine(img)
        drawCircle(img)
        drawEllipse(img)
        drawRectangle(img)
        writeImg(img)
    	display(img)

main()
