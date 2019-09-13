import numpy as np
import cv2

img = cv2.imread('main.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread('template.png', 0)

w, h = template.shape[::-1]
res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
loc = np.where(res >= 0.8)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0]+w,pt[1]+h), (0,255,255), 2)

cv2.imshow('res', cv2.resize(img, (800, 600)))
cv2.waitKey(0)
cv2.destroyAllWindows()
