import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame, = cap.read()
    if ret == True:
##        laplacian = cv2.Laplacian(frame, cv2.CV_64F)
##        sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
##        sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
        edges = cv2.Canny(frame, 40, 40)
        cv2.imshow('edges', edges)
##        cv2.imshow('original', frame)
##        cv2.imshow('laplacian', laplacian)
##        cv2.imshow('sobelx', sobelx)
##        cv2.imshow('sobely', sobely)
        if cv2.waitKey(5) & 0xFF == 27:
            break
    else:
        print 'ERROR - Camera couldn\'t find'

cap.release()
cv2.destroyAllWindows()
