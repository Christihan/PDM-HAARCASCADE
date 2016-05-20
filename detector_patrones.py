import cv2
import numpy as np
signal1_cascade = cv2.CascadeClassifier('signal1_cascade_v3.xml')
signal2_cascade = cv2.CascadeClassifier('signal2_cascade.xml')
signal3_cascade = cv2.CascadeClassifier('signal3_cascade2.xml')
cap = cv2.VideoCapture(0)
bandera=0
while 1:
    
    _,img = cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    signal1=signal1_cascade.detectMultiScale(gray,1.3,5)
    signal2=signal2_cascade.detectMultiScale(gray,1.3,5)
    signal3=signal3_cascade.detectMultiScale(gray,1.3,5)
    
    for (x,y,w,h) in signal1:
        #cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        if bandera==1:
            print "Detecto patron 1"
            bandera=0
    for (x,y,w,h) in signal2:
        #cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
        if bandera==1:
            print "Detecto patron 2"
            bandera=0
    for (x,y,w,h) in signal3:
        #cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
        if bandera==1:
            print "Detecto patron 3"
            bandera=0

    cv2.imshow('img',img)
    if (len(signal1) == 0)&(len(signal2) == 0)&(len(signal3) == 0)& (bandera ==0):
        print "No detecto patron"
        bandera =1
    k = cv2.waitKey(30)& 0xFF
    if k ==27:
        break
cv2.destroyAllWindows()
    
