import cv2
import numpy as np

def display(showimg):
    cv2.namedWindow('window',cv2.WINDOW_AUTOSIZE)
    cv2.imshow('window',showimg)
    cv2.waitKey(0)

def funcResize(img):
    ScaleX = .4
    ScaleY = .4
    scaleDown = cv2.resize(img,None,fx=int(200/240),fy=int(200/320),interpolation=cv2.INTER_LINEAR)
    display(scaleDown)
    

def funcCrop(img):
    cropped = img[50:250,20:290]
    display(cropped)

def funcRotate(img):
    dim = img.shape
    rotationAngle = -60
    scaleFactor = 1
    #getRotationMatrix2D take 3 argument
    #point of rotation
    #rotation angle 
    # Scale factor

    rotated = cv2.getRotationMatrix2D((dim[1]/2,dim[0]/2),rotationAngle,scaleFactor)
    
    result = cv2.warpAffine(img,rotated,(dim[1],dim[0]))
    display(result)

def main():
    img = cv2.imread(r'/home/dragonbreath/Downloads/n.jpeg',1)
    funcResize(img)
    funcCrop(img)
    funcRotate(img)

main()