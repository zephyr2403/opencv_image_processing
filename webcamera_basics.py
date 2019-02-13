import cv2

cap= cv2.VideoCapture(0) #0=> grab default camera


width = cap.get(cv2.CAP_PROP_FRAME_WIDTH) #returns float
height= cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
noFrame = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print('No of frame',noFrame)

# windows = *'DIVX'
#MACOS or LINUX XVID
writer = cv2.VideoWriter('/home/dragonbreath/Videos/znew.mp4',
cv2.VideoWriter_fourcc(*'XVID'), #CODEC
30,#number of frames
(int(width),int(height))
)
while True:
    #reading from cap 
    ret,frame = cap.read()
    #saving the frames
    writer.write(frame)

    cv2.imshow('frame',frame)
  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print(int(width),int(height))

cap.release()
writer.release()
cv2.destroyAllWindows()