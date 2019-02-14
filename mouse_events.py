import cv2
import numpy as np 
x1=0
y1=0
x2=0
y2=0
def drawRectangle(action,x,y,flags,userdata):
    global x1,y1,y2,x2,img
    if action == cv2.EVENT_LBUTTONDOWN:
        x1 =x 
        y1 =y
    elif action == cv2.EVENT_LBUTTONUP:
        x2 = x
        y2 = y
        cv2.rectangle(img,(x1,y1),(x2,y2),(40,42,40),thickness=2,lineType=cv2.LINE_AA)


img = cv2.imread(r'/home/dragonbreath/Pictures/tt.png',1)
if __name__ == '__main__':
    if img is None : 
        print "Error"
    else:
        cv2.namedWindow('window',cv2.WINDOW_AUTOSIZE)
        cv2.setMouseCallback('window',drawRectangle)
        k=0
        while k!=27:
            cv2.imshow('window',img)
            k = cv2.waitKey(20) & 0xFF
        cv2.destroyAllWindows()
