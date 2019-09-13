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
        
        kernel = np.ones((5,5), np.uint8)
        erosion = cv2.erode(mask, kernel, iterations=1)
        dilation = cv2.dilate(mask, kernel, iterations=1)
        #gradient = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel) erosion ve dilation birlesimi
        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        # opening - false positives ( background )
        # closing - false negatives ( foreground )
        blurRes = cv2.bitwise_and(opening, opening, mask=closing)
        
        cv2.imshow('res', res)
        cv2.imshow('blurRes', blurRes)
        cv2.imshow('opening', opening)
        cv2.imshow('closing', closing)
        #cv2.imshow('gradient', gradient)
##        cv2.imshow('erosion', erosion)
##        cv2.imshow('dilation', dilation)
        if cv2.waitKey(5) & 0xFF == 27:
            break
    else:
        print('ERROR - Camera couldn\'t find')

cap.release()
cv2.destroyAllWindows()
