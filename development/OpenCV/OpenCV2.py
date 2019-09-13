import numpy as np
import cv2

img = cv2.imread('dog.png')

cv2.line(img, (0,0), (300,300), (0,0,255), 5)
cv2.line(img, (300,0), (0,300), (0,0,255), 5)
cv2.rectangle(img, (0,0), (1,1), (0,128,255), -1)
cv2.circle(img, (75,110), 10, (128,0,64), -1)
cv2.circle(img, (152,125), 10, (128,0,64), -1)
pts = np.array([[0,20], [56,34], [234,50], [10,100]], np.int32)
cv2.polylines(img, [pts], True, (0,128,0), 10)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Opencv is Fun !', (30,40), font, 1, (255,255,255), 5, cv2.LINE_AA)
#cv2.putText(img, 'This is a text', (0,30), font, 1, (200,200,200), 3, cv2.LINE_AA)

cv2.imshow('window', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
