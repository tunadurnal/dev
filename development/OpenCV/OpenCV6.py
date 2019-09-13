import numpy as np
import cv2

img1 = cv2.imread('messi.png')
img2 = cv2.imread('mainlogo.png')

x = 456
y = 258
rows,cols,_ = img2.shape
x1 = int(x/2 + 10)
x2 = int(x1+rows)
y1 = int(y/2 + 65)
y2 = int(y1+cols)
roi = img1[x1:x2, y1:y2]

cv2.circle(img1, ((y1+y2)/2, (x1+x2)/2), 60, (255,255,255), -1)
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY)# black logo, white bg
mask_inv = cv2.bitwise_not(mask)# white logo, black bg
bg = cv2.bitwise_and(roi, roi, mask=mask)
fg = cv2.bitwise_and(img2, img2, mask=mask_inv)
dst = cv2.add(bg, fg)
img1[x1:x2, y1:y2] = dst
cv2.imshow('res', img1)

while True:
    if cv2.waitKey(5) & 0xFF == 27:
        cv2.destroyAllWindows()
        break
