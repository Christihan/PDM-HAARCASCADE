import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)
bandera=0
while 1:
    inicio=time.time()
    ret, img = cap.read()
    value1 = 134
    value2 = 0
    value3 = 21
    thresh = 51
    I_suma=np.sum(img,2)
    I_suma[I_suma==0]=1
    img_trf=np.zeros(img.shape,dtype=np.uint8)
    img_trf[:,:,0]=255.0*img[:,:,0]/(I_suma)
    img_trf[:,:,1]=255.0*img[:,:,1]/(I_suma)
    img_trf[:,:,2]=255.0*img[:,:,2]/(I_suma)
    B=img_trf[:,:,0]
    G=img_trf[:,:,1]
    R=img_trf[:,:,2]
    R[R>value1]=255
    G[R>value1]=0
    B[R>value1]=0
    R[G>value2]=0
    G[G>value2]=0
    B[G>value2]=0
    R[B>value3]=0
    G[B>value3]=0
    B[B>value3]=0
    img_trf[:,:,0]=B
    img_trf[:,:,1]=G
    img_trf[:,:,2]=R
    img_trf_gray = cv2.cvtColor(img_trf, cv2.COLOR_BGR2GRAY)
    _,img_bw=cv2.threshold(img_trf_gray,thresh,255,cv2.THRESH_BINARY)
    kernel=np.matrix('0,0,1,0,0;0,1,1,1,0;1,1,1,1,1;0,1,1,1,0;0,0,1,0,0',dtype='uint8')
    img_open= cv2.morphologyEx(img_bw, cv2.MORPH_OPEN, kernel)
    img_bw = cv2.morphologyEx(img_open, cv2.MORPH_CLOSE, kernel)
    moments=cv2.moments(img_bw)
    area=moments['m00']

    if(area > 180000):
        x=int(moments['m10']/moments['m00'])
        y=int(moments['m01']/moments['m00'])
        if(bandera==0):
            print "Se detecto objeto"
            bandera=1
        print "x = ", x
        print "y = ", y
    else:
        if(bandera==1):
            print "No se detecto objeto "
            bandera=0
    #final= time.time()-inicio
    #print final
    #cv2.imshow("Holi",img_bw)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
