import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    if ret == True:
        fgmask = fgbg.apply(frame)
        cv2.imshow('frame', frame)
        cv2.imshow('res', fgmask)
        if cv2.waitKey(5) & 0xff == 27:
            break
    else:
        print('ERROR')

cv2.destroyAllWindows()
    

