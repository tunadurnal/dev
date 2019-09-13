import numpy as np
import cv2

cap = cv2.VideoCapture(0)
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('video.avi', fourcc, 20, (w,h))

while True:
    ret, frame = cap.read()
    if ret == True:
        try:
            out.write(frame)
        except:
            print 'Error - Not writing to file'
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', frame)
        cv2.imshow('gray', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print 'Camera coulnd\'t find'

cap.release()
out.release()
cv2.destroyAllWindows()
