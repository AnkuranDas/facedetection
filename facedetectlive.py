# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 22:33:07 2019

@author: Ankuran Das
"""

import cv2
import time
video=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier("face.xml")
while True:
    
    time.sleep(3)
    check,frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray, scaleFactor= 1.05, minNeighbors=5)
    for x,y,w,h in faces:
        gray= cv2.rectangle(gray,(x,y), (x+w,y+h),(0,255,0),3)
    cv2.imshow("Capturing",gray)
    key=cv2.waitKey(1)
    if key ==ord('q'):
        break
video.release()
cv2.destroyAllWindows()