import numpy as np
import cv2

img1 = cv2.imread('messi.png')
img2 = cv2.imread('OpenCV_Logo.png')

rows, cols, _ = img2.shape
roi = img1[0:rows, 0:cols]

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

_, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
img_bg = cv2.bitwise_or(roi, roi, mask=mask)
img_fg = cv2.bitwise_or(img2, img2, mask=mask_inv)

dst = cv2.add(img_bg, img_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('res', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
