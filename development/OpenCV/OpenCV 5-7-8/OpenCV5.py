import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_color = np.array([70,145,50])
        upper_color = np.array([185,255,150])
        mask = cv2.inRange(hsv, lower_color, upper_color)
        res = cv2.bitwise_and(frame, frame, mask=mask)
        cv2.imshow('res', res)
        cv2.imshow('frame', frame)
        cv2.imshow('mask', mask)
        if cv2.waitKey(5) & 0xFF == 27:
            break
    else:
        print 'ERROR - Camera couldn\'t find'
cap.release()
cv2.destroyAllWindows()
