import numpy as np
import cv2

img = cv2.imread('bookpage.png')
grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 3)                       
#_,otsu = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)         
                       
cv2.imshow('img', img)
cv2.imshow('th', th)

cv2.waitKey(0)
cv2.destroyAllWindows()
