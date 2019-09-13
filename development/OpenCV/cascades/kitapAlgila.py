import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('../haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('../haarcascade_eye.xml')
c1 = cv2.CascadeClassifier('1.xml')
c2 = cv2.CascadeClassifier('2.xml')
c3 = cv2.CascadeClassifier('3.xml')
c4 = cv2.CascadeClassifier('4.xml')
c5 = cv2.CascadeClassifier('5.xml')
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    c1s = c1.detectMultiScale(gray, 6, 9)
    c2s = c2.detectMultiScale(gray, 6, 9)
    c3s = c3.detectMultiScale(gray, 6, 9)
    c4s = c4.detectMultiScale(gray, 6, 9)
    c5s = c5.detectMultiScale(gray, 6, 9)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    for (x1,y1,w1,h1) in c1s:
        cv2.putText(frame, 'Ispanyolca Kitabi', (x1-w1, y1-h1), font, 0.5, (0,255,255), 2, cv2.LINE_AA)
    for (x2,y2,w2,h2) in c2s:
        cv2.putText(frame, 'Ispanyolca Kitabi', (x2-w2, y2-h2), font, 0.5, (0,255,255), 2, cv2.LINE_AA)
    for (x3,y3,w3,h3) in c3s:
        cv2.putText(frame, 'Ispanyolca Kitabi', (x3-w3, y3-h3), font, 0.5, (0,255,255), 2, cv2.LINE_AA)
    for (x4,y4,w4,h4) in c4s:
        cv2.putText(frame, 'Ispanyolca Kitabi', (x4-w4, y4-h4), font, 0.5, (0,255,255), 2, cv2.LINE_AA)
    for (x5,y5,w5,h5) in c5s:
        cv2.putText(frame, 'Ispanyolca Kitabi', (x5-w5, y5-h5), font, 0.5, (0,255,255), 2, cv2.LINE_AA)
    cv2.imshow('res', frame)
    if cv2.waitKey(5) & 0xff == 27:
        break

cap.release()
cv2.destroyAllWindows()






















        
