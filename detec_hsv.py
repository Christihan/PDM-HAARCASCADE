import cv2
import numpy as np
import time
#Iniciamos la camara
captura = cv2.VideoCapture(0)
bandera=0
while(1):
    inicio=time.time()
    #Capturamos una imagen y la convertimos de RGB -> HSV
    _, imagen = captura.read()
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
 
    #Establecemos el rango de colores que vamos a detectar
    #En este caso de rojo oscuro a rojo claro
    rojo_bajos = np.array([158,149,149], dtype=np.uint8)
    rojo_altos = np.array([180,255,219], dtype=np.uint8)
    
    #Crear una mascara con solo los pixeles dentro del rango de rojos
    mask = cv2.inRange(hsv, rojo_bajos, rojo_altos)
    kernel=np.matrix('0,0,1,0,0;0,1,1,1,0;1,1,1,1,1;0,1,1,1,0;0,0,1,0,0',dtype=np.uint8)
    mask=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
    #mask=cv2.dilate(mask,None,iterations=3)
 
    #Encontrar el area de los objetos que detecta la camara
    moments = cv2.moments(mask)
    area = moments['m00']
 
    #Descomentar para ver el area por pantalla
    #print area
    if(area > 200000):
        if(bandera==0):
            print "Se detecto objeto"
            bandera=1
        #Buscamos el centro x, y del objeto
        x = int(moments['m10']/moments['m00'])
        y = int(moments['m01']/moments['m00'])
         
        #Mostramos sus coordenadas por pantalla
        print "x = ", x
        print "y = ", y
    else:
        if(bandera==1):
            print "No se detecto objeto "
            bandera=0
        #Dibujamos una marca en el centro del objeto
        #cv2.rectangle(imagen, (x-5, y-5), (x+5, y+5),(0,0,255), 2)
        #cv2.putText(imagen, "pos:"+ str(x)+","+str(y), (x+10,y+10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
     
    #Mostramos la imagen original con la marca del centro y
    #la mascara
    #cv2.imshow('mask', mask)
    #cv2.imshow('Camara', imagen)
    #final=time.time()-inicio
    #print final
    #tecla = cv2.waitKey(5) & 0xFF
    if cv2.waitKey(1) & 0xFF == ord('q'):
        captura.release()
        break 
cv2.destroyAllWindows()
