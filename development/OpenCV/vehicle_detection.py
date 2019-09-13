import cv2
import numpy as np

car_cascade = cv2.CascadeClassifier('cars.xml')
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow('video', frame)
    if cv2.waitKey(5) == 27:
        break

cv2.destroyAllWindows()

