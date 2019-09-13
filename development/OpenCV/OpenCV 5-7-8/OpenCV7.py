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
        median = cv2.medianBlur(res, 5)
        cv2.imshow('res', res)
        cv2.imshow('median', median)

##        kernel = np.ones((5,5))/25
##        smoothed = cv2.filter2D(res, -1, kernel)
        
        #blur = cv2.GaussianBlur(res, (5,5), 0)
        #bilateral = cv2.bilateralFilter(res, 5, 75, 75)
##        cv2.imshow('bilateral', bilateral)
##        cv2.imshow('blur', blur)
##        cv2.imshow('smoothed', smoothed)
##        cv2.imshow('frame', frame)
        if cv2.waitKey(5) & 0xFF == 27:
            break
    else:
        print 'ERROR - Camera couldn\'t find'

cap.release()
cv2.destroyAllWindows()
