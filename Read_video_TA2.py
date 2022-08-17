import cv2
vid=cv2.VideoCapture("AnthonyShkraba.mp4")

if(vid.isOpened()==False):
    print("Unable to read feed")
else:
    print("OPENED")

height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(height)

width= int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
print(width)

fps=int(vid.get(cv2.CAP_PROP_FPS))
print(fps)

while(True):
    ret,frame=vid.read()
    cv2.imshow("WEbcam",frame)
    #cv2.waitKey(25)
    if cv2.waitKey(25)==32:
        break
vid.release()
cv2.destroyAllWindows()    
