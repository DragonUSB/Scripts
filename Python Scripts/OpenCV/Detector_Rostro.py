import cv2
import numpy as np
import os
import platform

absolute_path = os.path.dirname(__file__)
sistema = platform.system()

if sistema == 'Linux':
    file = absolute_path + '/Oficina.png'
else:
    file = absolute_path + '\Oficina.png'

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

imagen = cv2.imread(file)
gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

faces = faceClassif.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30,30), maxSize=(200,200))

for (x,y,w,h) in faces:
	cv2.rectangle(imagen,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow('imagen',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()